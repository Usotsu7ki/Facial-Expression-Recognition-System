# server.py
import socket
import threading
import cv2
import numpy as np

# 服务器IP和端口配置
SERVER_IP = ''
SERVER_PORT = 8080



# 客户端和管理员的套接字列表
client_sockets = []
admin_sock = None



def load_admin_password():
    try:
        with open('password.txt', 'r') as file:
            return file.readline().strip()  # 读取第一行并去除可能的前后空白字符
    except Exception as e:
        print(f"Error loading admin password: {e}")
        return None

def client_handler(client_sock, client_address):
    global admin_sock
    print("client handler")
    while True:
        try:
            # 接收客户端发送的信息
            message = client_sock.recv(1024).decode()
            if message.startswith("password:"):
                _, password = message.split(":")
                print(f"password: {password}")
                if password == ADMIN_PASSWORD:
                    # 如果是管理员密码，发送确认消息(主界面接收并打开admin界面)
                    client_sockets.append(client_sock)
                    admin_sock = client_sock
                    client_sock.send("admin".encode())
                    print(f"管理员 {client_address} 已连接。")
                    handle_admin(client_sock)
                    break
                else:
                    client_sock.send("password false".encode())
            elif message == "client":
                # 客户端请求跳过登录，进入普通客户端处理逻辑
                print("client require to connect")
                client_sockets.append(client_sock)
                handle_client(client_sock,client_address)
                break
            else:
                print(f"未知消息 {message} 从 {client_address} 收到。")
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
    is_connected = True

    client_sock.send("ok".encode())
    if admin_sock:
        send_client_list_to_admin(admin_sock)
    try:
        while is_connected:
            length_str = b""
            char = client_sock.recv(1)
            if char == b'':
                is_connected = False
                print("Client disconnected1")
                continue
            while char != b'\n':
                length_str += char
                char = client_sock.recv(1)
                if char == b'':
                    is_connected = False
                    print("Client disconnected2")
                    break

            if length_str == b'close': #收到close命令后停止接收处理图像(但是不停socket)
                is_connected = False
                print("Client requested to close the connection")
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
            cv2.imshow("img", img)
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



def handle_admin(admin_socket): #要像client一样退出后回去
    global admin_sock
    is_admin_connected = True
    message = admin_socket.recv(1024).decode()
    print(f"message from admin: {message}")
    send_client_list_to_admin(admin_socket)
    try:
        while is_admin_connected:
            message = admin_socket.recv(1024).decode()
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
        try:
            admin_sock.close()
        except Exception as e:
            print(f"close admin socket fail{e}")
        if admin_socket in client_sockets:
            client_sockets.remove(admin_socket)
        admin_sock = None




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
        threading.Thread(target=client_handler, args=(client_sock, client_address)).start()

def main():
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
