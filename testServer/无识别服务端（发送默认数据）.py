# 无识别服务端（发送默认数据）.py
#from main import *
import os
import argparse

# from models.PosterV2_7cls import *
import time


import socket
import threading
import cv2
import numpy as np
import sqlite3



# 服务器IP和端口配置
SERVER_IP = ''
SERVER_PORT = 8080

DATABASE_FILE = 'server_database.db'

# 客户端和管理员的套接字列表
client_sockets = []
admin_sock = None

# 暂时定义一个管理员注册码为12345678
correct_admin_number = 12345678




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
        #判断密码
        if password == stored_password:
            #判断是否有admin码
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
    print("注册用户")
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    try:
        cursor.execute('''
        INSERT INTO users (username, password, security_question, security_answer, admin_number)
        VALUES (?, ?, ?, ?, ?)''', (username, password, security_question, security_answer, admin_number))
        conn.commit()
        print("注册完毕")
        return True
    except sqlite3.IntegrityError:
        return False
    except Exception as e:
        print(f"Database error: {e}")
        return False
    finally:
        conn.close()

# 验证用户名是否已存在
def username_exists(username):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM users WHERE username=?', (username,))
    user = cursor.fetchone()
    conn.close()
    return user is not None

def load_admin_password():
    try:
        with open('password.txt', 'r') as file:
            return file.readline().strip()  # 读取第一行并去除可能的前后空白字符
    except Exception as e:
        print(f"Error loading admin password: {e}")
        return None

def client_handler(client_sock, client_address):
    # clear_socket_buffer(client_sock)
    global admin_sock
    print("client handler")
    while True:
        try:
            # 接收客户端发送的信息
            message = client_sock.recv(1024).decode()
############################第一个分支，login#############################################
            if message.startswith("login:"):
                _, username, password = message.split(":", 2)
                # 收到后进行用户名和密码的验证
                user_verified, is_admin = verify_user_credentials(username, password)
                if user_verified:
                    if is_admin:
                        # 如果是管理员，发送确认消息(主界面接收并打开admin界面)
                        print("admin require to connect")
                        client_sockets.append(client_sock)
                        admin_sock = client_sock
                        client_sock.send("admin".encode())
                        print(f"管理员 {client_address} 已连接。")
                        handle_admin(client_sock,client_address)
                        break
                    else:
                        # 不是管理员，进入普通客户端处理逻辑
                        print("client require to connect")
                        client_sock.send("client".encode())
                        client_sockets.append(client_sock)
                        handle_client(client_sock, client_address)
                        break
                else:
                    client_sock.send("fail".encode())
############################第二个分支，register#############################################
            elif message.startswith("register:"):
                print("user want to register")
                _, registration_info = message.split("register:", 1)
                username, password, security_question, security_answer, admin_number = registration_info.split("|")

                # 如果提供了 admin_number，需要验证
                if admin_number and admin_number != str(correct_admin_number):
                    print("admin number incorrect")
                    client_sock.send("fail_admin".encode())
                    continue

                # 检查用户名是否已存在
                if username_exists(username):
                    print("username duplicate")
                    client_sock.send("fail_username_same".encode())
                    continue

                # 注册用户
                if register_user(username, password, security_question, security_answer, admin_number):
                    print("register success")
                    client_sock.send("register success".encode())
                else:
                    print("fail in database")
                    client_sock.send("fail_database".encode())
                    continue
############################第三个分支，获取密保#############################################
            elif message.startswith("forget:"):
                username = message.split(":", 1)[1]
                security_question = get_security_question(username)
                if security_question:
                    client_sock.send(security_question.encode())
                else:
                    client_sock.send("username_notexist".encode())
############################第四个分支，修改密码#############################################
            elif message.startswith("change:"):
                _, username, security_answer, new_password = message.split(":", 3)
                if verify_security_answer(username, security_answer):
                    if update_password(username, new_password):
                        client_sock.send("success".encode())
                    else:
                        client_sock.send("fail_database".encode())
                else:
                    client_sock.send("fail".encode())
            elif message.startswith('d'):
                receiving_processing(client_sock,client_address)
############################其他分支#############################################
            elif message == 'close':
                client_handler(client_sock,client_address)
                return
            else:
                print(f"未知消息 {message} 从 {client_address} 收到,可能是断开连接")
                break
        except ConnectionResetError:
            # 客户端断开连接
            print(f"客户端 {client_address} 断开连接。")
            try:
                client_sockets.remove(client_sock)
            except Exception as e:
                print("error from remove from clients list when the client disconnect"+str(e))
            break

def handle_client(client_sock,client_address):
    # 处理普通客户端的函数
    # 这里可以处理客户端发送的图像并发送回响应
    print("handling client")

    message = client_sock.recv(1024).decode()#用于等阻塞客户端的Qmessagebox
    print(message)
    if(message=='back'):
        client_handler(client_sock, client_address)
        print("back")
        return
    client_sock.send("ok".encode())
    if admin_sock:
        send_client_list_to_admin(admin_sock)
    receiving_processing(client_sock,client_address)

def receiving_processing(client_sock,client_address):
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
            while char != b'\n' and char !=b'd':
                length_str += char
                char = client_sock.recv(1)
                if char == b'':
                    is_connected = False
                    print("Client disconnected2")
                    break

            if length_str == b'close': #收到close命令后停止接收处理图像(但是不停socket)
                is_connected = False
                print("Client requested to close the connection")
                clear_socket_buffer(client_sock)
                continue

            total = int(length_str)

            # 然后根据长度接收图像数据
            img_bytes = client_sock.recv(total)
            while len(img_bytes) < total:
                img_bytes += client_sock.recv(total - len(img_bytes))

            # 解析接收到的字节流数据，并显示图像
            img = np.frombuffer(img_bytes, dtype=np.uint8)
            img = cv2.imdecode(img, cv2.IMREAD_COLOR)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # print(img)
            start_time = time.time()
            #faces = detector(img, 0)

            send_message = "B:Smile 0.999 250 150 200 200"
            # for face in faces:
            #     x, y, w, h = face.left(), face.top(), face.width(), face.height()
            #     # 提取人脸ROI
            #     face_roi = img[y:y + h, x:x + w]
            #     face_pil = Image.fromarray(cv2.cvtColor(face_roi, cv2.COLOR_BGR2RGB))
            #     face_tensor = tran(face_pil).unsqueeze(0).cuda()  # 将输入数据移到GPU
            #
            #     # 进行推理
            #     with torch.no_grad():
            #         output = model(face_tensor)
            #         probs = F.softmax(output, dim=1).squeeze().cpu().numpy()
            #     _, predicted_class = torch.max(output, 1)
            #     # print(predicted_class)
            #     predicted_label = classes[predicted_class]
            #
            #     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            #     # cv2.putText(img, f'{predicted_label}: {probs[predicted_class]:.2f}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1,
            #     #             (0, 255, 0), 2)
            #     send_message = send_message+f'{predicted_label} '+f'{probs[predicted_class]:.3f} '+f'{x} {y} {w} {h},'
            #     # 添加每个类别的概率文本
            #     # y_offset = y + h + 20
            #     # for i, prob in enumerate(probs):
            #     #     cv2.putText(img, f'{classes[i]}: {prob:.8f}', (x, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
            #     #                 (255, 255, 255), 1)
            #     #     y_offset += 20  # 调整文本的垂直位置
            #
            #     # cv2.imshow('frame', img)
            time.sleep(0.2)
            end_time = time.time()
            execution_time = end_time - start_time
            cv2.imshow('frame', img)
            print("Code execution time: {:.2f} seconds".format(execution_time))

            client_sock.send(send_message.encode())
            print("send end")


            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


    except Exception as e:
        print("receiving and processing error：" + str(e))
    finally:
        cv2.destroyAllWindows()
        print("connection close, wait for new connection")
        client_sockets.remove(client_sock)
        if admin_sock:
            send_client_list_to_admin(admin_sock)
        client_handler(client_sock,client_address)


def handle_admin(admin_socket_me,admin_address): #要像client一样退出后回去
    global admin_sock
    is_admin_connected = True
    message = admin_socket_me.recv(1024).decode()
    print(f"message from admin: {message}")
    send_client_list_to_admin(admin_socket_me)
    try:
        while is_admin_connected:
            message = admin_socket_me.recv(1024).decode()
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
        if admin_socket_me in client_sockets:
            client_sockets.remove(admin_socket_me)
        is_admin_connected = False
        admin_sock=None
        client_handler(admin_socket_me, admin_address)



def kick_client(client_address):
    print(f"kick_client begin:{client_address}")
    for client in client_sockets:
        if str(client.getpeername()) == client_address:
            client.send("disconnect".encode())
            print(f"Kicked client {client_address}")
            break

def send_message_to_client(client_address, msg):
    for client in client_sockets:
        if str(client.getpeername()) == client_address:
            client.send(msg.encode())
            print(f"Sent message to {client_address}")
            break




def send_client_list_to_admin(admin_sock):
    print(f"begin send list: {client_sockets}")
    #把已连接的客户端列表发送给admin
    client_addresses = []
    for client in client_sockets:
        address = str(client.getpeername())
        client_addresses.append(address)
    client_addresses_str = "\n".join(client_addresses)  # 使用换行符将地址连接成一个字符串
    admin_sock.send(client_addresses_str.encode())
    print("send end")


def accept_connections(server_socket):
    while True:
        client_sock, client_address = server_socket.accept()
        print(f"客户端 {client_address} 已连接。")
        # every client
        threading.Thread(target=client_handler, args=(client_sock, client_address)).start()

def clear_socket_buffer(sock):
    """尝试非阻塞地读取socket，以清理可能残留的数据。"""
    sock.setblocking(0)  # 设置socket为非阻塞模式
    try:
        while True:
            data = sock.recv(1024)
            if not data:
                break  # 如果没有更多数据，跳出循环
    except BlockingIOError:
        # 如果没有数据可读，会抛出BlockingIOError错误
        pass
    finally:
        sock.setblocking(1)  # 将socket重置为阻塞模式

def main():
    setup_database()
    global ADMIN_PASSWORD
    ADMIN_PASSWORD = load_admin_password()
    if ADMIN_PASSWORD is None:
        print("Admin password could not be loaded.")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen()
    print(f"服务器启动，等待连接到 {SERVER_IP}:{SERVER_PORT}...")
    accept_connections(server_socket)

if __name__ == '__main__':
    main()
