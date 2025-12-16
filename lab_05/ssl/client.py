import socket
import ssl
import threading

server_address = ('localhost', 12345)

def receive_data(ssl_socket):
    try:
        while True:
            data = ssl_socket.recv(1024)
            if not data:
                break
            print("Nhận:", data.decode('utf-8'))
    except Exception as e:
        print("Lỗi nhận:", e)
    finally:
        ssl_socket.close()
        print("Kết nối đã đóng.")

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    ssl_socket = context.wrap_socket(client_socket, server_hostname='localhost')
    ssl_socket.connect(server_address)

    threading.Thread(target=receive_data, args=(ssl_socket,), daemon=True).start()

    try:
        while True:
            message = input("Nhập tin nhắn: ")
            ssl_socket.sendall(message.encode('utf-8'))
    except KeyboardInterrupt:
        pass
    finally:
        ssl_socket.close()

if __name__ == "__main__":
    main()
