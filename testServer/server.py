# 无识别服务端（发送默认数据）.py
from main import *
import os
import argparse

from models.PosterV2_7cls import *
import time
import torch.nn.parallel
import torch.optim
import torch.utils.data
import torch.utils.data.distributed
import torchvision.transforms as transforms
import dlib
import socket
import threading
import cv2
import numpy as np
import sqlite3
from PIL import Image


# The ip and port
SERVER_IP = ''
SERVER_PORT = 8080

# the database name
DATABASE_FILE = 'server_database.db'

# connected client socket lists
client_sockets = []
admin_sock = None

# you can change it freely, we set it as 12345678(you should change it in the password.txt, not here)
correct_admin_number = 12345678


classes = ('Surprise', 'fear', 'disgust', 'smile','sadness', 'anger', 'Neutral')
tran = transforms.Compose([transforms.Resize((224, 224)),
                           transforms.ToTensor(),
                           transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                                std=[0.229, 0.224, 0.225]),
                           ])

os.environ["CUDA_VISIBLE_DEVICES"] = '0'
model = pyramid_trans_expr2(img_size=224, num_classes=7)
model = torch.nn.DataParallel(model).cuda()
criterion = torch.nn.CrossEntropyLoss()
checkpoint = torch.load(r'C:\Users\hp\Desktop\Facial-Expression-Recognition-System-serverClient\testServer\checkpoint\raf-db-model_best.pth')
model.load_state_dict(checkpoint['state_dict'])
model.eval()
detector = dlib.cnn_face_detection_model_v1(r'C:\Users\hp\Desktop\Facial-Expression-Recognition-System-serverClient\testServer\checkpoint\mmod_human_face_detector.dat')
# detector = dlib.get_frontal_face_detector()
print(torch.cuda.is_available())


def verify_security_answer(username, security_answer):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT security_answer FROM users WHERE username=?", (username,))
        answer = cursor.fetchone()
        if answer and answer[0] == security_answer:
            return True
        else:
            return False
    finally:
        conn.close()


def update_password(username, new_password):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE users SET password=? WHERE username=?", (new_password, username))
        conn.commit()
        return True
    except sqlite3.Error:
        return False
    finally:
        conn.close()



def get_security_question(username):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT security_question FROM users WHERE username=?", (username,))
        question = cursor.fetchone()
        if question:
            return question[0]
        else:
            return None
    finally:
        conn.close()



def verify_user_credentials(username, password):
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    cursor.execute("SELECT password, admin_number FROM users WHERE username=?", (username,))
    user_record = cursor.fetchone()

    connection.close()

    if user_record:
        stored_password, admin_number = user_record
        if password == stored_password:
            if admin_number:
                is_admin = True
            else:
                is_admin = False
            return True, is_admin
        else:
            return False, False
    else:
        return False, False



def setup_database():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        security_question TEXT NOT NULL,
        security_answer TEXT NOT NULL,
        admin_number TEXT
    )''')
    conn.commit()
    conn.close()

def register_user(username, password, security_question, security_answer, admin_number):
    print("Register for user")
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    try:
        cursor.execute('''
        INSERT INTO users (username, password, security_question, security_answer, admin_number)
        VALUES (?, ?, ?, ?, ?)''', (username, password, security_question, security_answer, admin_number))
        conn.commit()
        print("register complete")
        return True
    except sqlite3.IntegrityError:
        return False
    except Exception as e:
        print(f"Database error: {e}")
        return False
    finally:
        conn.close()

# during registration, check whether the username exists
def username_exists(username):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM users WHERE username=?', (username,))
    user = cursor.fetchone()
    conn.close()
    if user is not None:
        return True
    else:
        return False

def load_admin_password():
    try:
        with open('password.txt', 'r') as file:
            return file.readline().strip()
    except Exception as e:
        print(f"Error loading admin password: {e}")
        return None


# For every client connection a new thread executing this method will start
# During this method, client will be in the menu, there are 5 kind of messages that it may send to here
# This method is used to judge the messages and execute different methods
def client_handler(client_sock, client_address):
    # clear_socket_buffer(client_sock)
    global admin_sock
    print("client handler")
    while True:
        try:
            # client is in
            message = client_sock.recv(1024).decode()
############################first situation: the clikent want to login#############################################
            if message.startswith("login:"):
                _, username, password = message.split(":", 2)
                # received username and password
                user_verified, is_admin = verify_user_credentials(username, password)
                if user_verified:
                    if is_admin:
                        # if the account is admin, send message to verify login as admin
                        print("admin require to connect")
                        # client_sockets.append(client_sock)
                        admin_sock = client_sock
                        client_sock.send("admin".encode())
                        print(f"administrator {client_address} is connected。")
                        handle_admin(client_sock,client_address)
                        break
                    else:
                        # not admin, the client-side is a normal client
                        print("client require to connect")
                        client_sock.send("client".encode())
                        # client_sockets.append(client_sock)
                        handle_client(client_sock, client_address)
                        break
                else:
                    client_sock.send("fail".encode())
############################the second situation: the user want to register#############################################
            elif message.startswith("register:"):
                print("user want to register")
                _, registration_info = message.split("register:", 1)
                username, password, security_question, security_answer, admin_number = registration_info.split("|")

                # if he/she provide admin code, check it
                if admin_number and admin_number != str(correct_admin_number):
                    print("admin number incorrect")
                    client_sock.send("fail_admin".encode())
                    continue

                # check whether the username exists
                if username_exists(username):
                    print("username duplicate")
                    client_sock.send("fail_username_same".encode())
                    continue

                # register the account for the user
                if register_user(username, password, security_question, security_answer, admin_number):
                    print("register success")
                    client_sock.send("register success".encode())
                else:
                    print("fail in database")
                    client_sock.send("fail_database".encode())
                    continue
############################the third situation: the user want to reset pwd, ask for security question firstly#############################################
            elif message.startswith("forget:"):
                username = message.split(":", 1)[1]
                security_question = get_security_question(username)
                if security_question:
                    client_sock.send(security_question.encode())
                else:
                    client_sock.send("username_notexist".encode())
############################the forth situation: the user want to reset pwd, with the security answer#############################################
            elif message.startswith("change:"):
                _, username, security_answer, new_password = message.split(":", 3)
                if verify_security_answer(username, security_answer):
                    if update_password(username, new_password):
                        client_sock.send("success".encode())
                    else:
                        client_sock.send("fail_database".encode())
                else:
                    client_sock.send("fail".encode())
#############################special situation, continue processing#############################################
            elif message.startswith('d'):
                receiving_processing(client_sock,client_address)
############################other situation, including the client close#############################################
            elif message == 'close':
                client_handler(client_sock,client_address)
                return
            else:
                print(f"unknown {message} from {client_address} , usually it means disconnected ")
                break
        except ConnectionResetError:
            # the client disconnected
            print(f"client {client_address} disconnected")
            try:
                client_sockets.remove(client_sock)
            except Exception as e:
                print("error from remove from clients list when the client disconnect"+str(e))
            break

def handle_client(client_sock,client_address):
    # this is used to handle client
    print("handling client")

    message = client_sock.recv(1024).decode()
    print(message)
    if(message=='back'):
        client_handler(client_sock, client_address)
        print("back")
        return
    client_sock.send("ok".encode())
    client_sockets.append(client_sock) #add the client to the list
    if admin_sock:
        send_client_list_to_admin(admin_sock) # and ask admin to update the list
    receiving_processing(client_sock,client_address)



# This method receive images from client, processing and send results
def receiving_processing(client_sock, client_address):
    is_connected = True
    try:
        while is_connected:
            print("listening")
            length_str = b""
            char = client_sock.recv(1)
            if char == b'':
                is_connected = False
                print("Client disconnected1")
                continue
            while char != b'\n' and char != b'd':
                length_str += char
                char = client_sock.recv(1)
                if char == b'':
                    is_connected = False
                    print("Client disconnected2")
                    break

            if length_str == b'close':  # after receiving close, stop receiving(client back or close), back to client_handler
                is_connected = False
                print("Client requested to close the connection")
                # clear_socket_buffer(client_sock)
                continue

            total = int(length_str)

            # receive image according to the length
            img_bytes = client_sock.recv(total)
            while len(img_bytes) < total:
                img_bytes += client_sock.recv(total - len(img_bytes))

            # Parse the received byte stream data and display the image
            img = np.frombuffer(img_bytes, dtype=np.uint8)
            img = cv2.imdecode(img, cv2.IMREAD_COLOR)
            # Record the time before starting to process the image
            start_time = time.time()
            # Initialize the parameters sent to the client,B: is for Begin
            send_message = "B:"
            # Face detection model detects faces
            faces = detector(img, 0)
            # A list that stores tensor information of faces
            tensor_list = []
            # A list that stores the location of faces in the image
            position_list = []
            # Classify expressions on each face in the picture
            for face in faces:
                rect = face.rect
                x, y, w, h = rect.left(), rect.top(), rect.width(), rect.height()
                face_roi = img[y:y + h, x:x + w]
                try:
                    # If the face returned by the detector cannot be converted to RGB
                    face_pil = Image.fromarray(cv2.cvtColor(face_roi, cv2.COLOR_BGR2RGB))
                    tensor_list.append(tran(face_pil).unsqueeze(0).cuda())
                    position_list.append([x, y, w, h])
                except Exception as e:
                    print(f"The face shake is too large, please try again!")
                    continue

            if len(tensor_list) != 0:
                """Put the faces separated by the detection model into the one
                dimension so that they can be used as the input of the model in the same batch"""
                input = torch.cat(tensor_list, dim=0)
                with torch.no_grad():
                    output = model(input)
                    probs = F.softmax(output, dim=1).squeeze().cpu().numpy()
                _, predicted_class = torch.max(output, 1)
                if probs.ndim == 1:
                    max_probs = [np.max(probs)]
                else:
                    max_probs = np.amax(probs, axis=1)
                send_message = send_message + (
                            str(predicted_class.tolist()) + '|' + str([f'{x:.3f}' for x in max_probs]) + '|' + str(
                        position_list) + '|')
                send_message = send_message.replace("[", "")
                send_message = send_message.replace("]", "")
                print(classes[predicted_class])
            else:
                print("There is no face")
            end_time = time.time()
            execution_time = end_time - start_time
            print("Code execution time: {:.2f} seconds".format(execution_time))
            print(send_message)
            client_sock.send(send_message.encode())

    except Exception as e:
        print("receiving and processing error：" + str(e))
    finally:
        cv2.destroyAllWindows()
        print("connection close, wait for new connection")
        client_sockets.remove(client_sock) # remove it from client_list
        if admin_sock:
            send_client_list_to_admin(admin_sock)
        client_handler(client_sock, client_address) # re-execute client_handler(because this usually means client close, or disconnect)


def handle_admin(admin_socket_me,admin_address): #this is used to handle connection with admin
    global admin_sock
    is_admin_connected = True
    message = admin_socket_me.recv(1024).decode() # confirm with admin, ensure chatting with admin now
    print(f"message from admin: {message}")
    send_client_list_to_admin(admin_socket_me) # send client lists to admin
    try:
        while is_admin_connected:
            message = admin_socket_me.recv(1024).decode() #keep listening messages from admin
            if message == "close":
                is_admin_connected = False
                continue
            elif message.startswith("kick"):
                _, client_address = message.split(":")
                kick_client(client_address)
            elif message.startswith("sendmessage"):
                _, client_address, msg = message.split("|", 2)
                send_message_to_client(client_address, msg)
    except Exception as e:
        print(f"Error handling admin message: {e}")
    finally:
        print("connection close, wait for new connection")
        if admin_socket_me in client_sockets: # remove the admin from connected list
            client_sockets.remove(admin_socket_me)
        is_admin_connected = False
        admin_sock=None
        client_handler(admin_socket_me, admin_address) # continue listening



def kick_client(client_address): # send disconnect to the client to make it quit camera window
    print(f"kick_client begin:{client_address}")
    for client in client_sockets:
        if str(client.getpeername()) == client_address:
            client.send("disconnect".encode())
            if client in client_sockets:        # remove it from connected client list
                client_sockets.remove(client)
            print(f"Kicked client {client_address}")
            break

def send_message_to_client(client_address, msg): # send message to client
    for client in client_sockets:
        if str(client.getpeername()) == client_address:
            client.send(msg.encode())
            print(f"Sent message to {client_address}")
            break




def send_client_list_to_admin(admin_sock):
    print(f"begin send list: {client_sockets}")
    # send the client list to the admin
    client_addresses = []
    for client in client_sockets:
        address = str(client.getpeername())
        client_addresses.append(address)
    client_addresses_str = "\n".join(client_addresses)
    admin_sock.send(client_addresses_str.encode())
    print("send end")


def accept_connections(server_socket):
    while True:
        client_sock, client_address = server_socket.accept()
        print(f"client {client_address} is connected。")
        # for every client, create a thread to listen messages from ir
        threading.Thread(target=client_handler, args=(client_sock, client_address)).start()

def main():
    setup_database() # set up the database
    global ADMIN_PASSWORD # this is admin code
    ADMIN_PASSWORD = load_admin_password()
    if ADMIN_PASSWORD is None:
        print("Admin password could not be loaded.")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen()
    print(f"Server launched，wait connection to {SERVER_IP}:{SERVER_PORT}...")
    accept_connections(server_socket)

if __name__ == '__main__':
    main()
