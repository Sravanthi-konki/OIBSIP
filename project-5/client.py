import socket
import threading

def receive_messages(client_socket)
try:
while True:
    message = client_socket.recv(1024).decode('utf-8')
    print(message)
except Exception as e:
        print(f"Error receiving message: {e}")

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 5555))

    username = input("Enter your username: ")
    client.send(username.encode('utf-8'))

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    try:
        while True:
            message= input()
            client.send(f"{username}: {message}".encode('utf-8'))

    except KeyboardInterrupt:
        client.close()
if __name__ == "__main__":
    main()
