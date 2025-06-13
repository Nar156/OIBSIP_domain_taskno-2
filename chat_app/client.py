import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

def recieve_mess(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"\n[NEW MESSAGE] {message}")
            else:
                break
        except:
            break

def send_message(client_socket):
    while True:
        message = input("")
        if message.lower() == "exit":
            client_socket.close()
            break
        client_socket.send(message.encode('utf-8'))

def start_client():
    start_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    start_client.connect((HOST, PORT))

    recieve_thread = threading.Thread(target=recieve_mess, args=(start_client,))
    recieve_thread.start()

    send_message(start_client)

if __name__ == "__main__":
    start_client()