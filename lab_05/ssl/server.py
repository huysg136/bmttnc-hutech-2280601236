import socket
import ssl
import threading
import base64

server_address = ('localhost', 12345)
clients = []

def handle_client(client_socket):
    clients.append(client_socket)

    print("Đã kết nối với:", client_socket.getpeername())

    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            
            try:
                decoded_data = base64.b64decode(data.strip()).decode('utf-8')
                print("Nhận:", decoded_data)
            except:
                print("Nhận:", data.decode('utf-8'))
        
            for client in clients:
                if client != client_socket:
                    try:
                        client.send(data)
                    except:
                        clients.remove(client)

    except Exception as e:
        print(f"Lỗi xử lý client {client_socket.getpeername()}: {e}")
        
    finally:
        print("Đã ngắt kết nối:", client_socket.getpeername())
        try:
            clients.remove(client_socket)
        except ValueError:
            pass 
        try:
            client_socket.close()
        except:
            pass 

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_address)
    server_socket.listen(5)
    print("Server đang chờ kết nối...")

    while True:
        try:
            client_socket, client_address = server_socket.accept()
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            context.load_cert_chain(
                certfile=r"D:\PracticeAIS\lab_05\ssl\certificates\server-cert.crt",
                keyfile=r"D:\PracticeAIS\lab_05\ssl\certificates\server-key.key"
            )
            ssl_socket = context.wrap_socket(client_socket, server_side=True)
            client_thread = threading.Thread(target=handle_client, args=(ssl_socket,))
            client_thread.start()
        except KeyboardInterrupt:
            print("\nServer shutting down...")
            break
        except Exception as e:
            print(f"Lỗi chấp nhận kết nối: {e}")
            break

    server_socket.close()

if __name__ == "__main__":
    main()