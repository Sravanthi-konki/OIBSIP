import socket
import threading

def handle_client(client_socket, addr, clients):
    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Received from {addr}: {message}")
            broadcast(message,client)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        clients.remove(client_socket)

def broadcast(message,clients):
    for client in clients:
        try:
            client.send(message.enocde('utf-8'))
        except Exception as e:
            print(f"Error broadcasting message: {e}")
def main():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('0.0.0.0',5555))
    server.listen(5)

    print("Chat Server is listening on port 5555")

    clients = [] 
    while True:
        client_socket,addr = server.accept()
        clients.append(client_socket)

        print(f"Accepted connection from {addr}")
        client_handler =  threading.Thread(target= handle_client, args = (client_socket,addr,clients))
        client_handler.start()
if __name__ == "__main__":
    main()   