import socket
import threading
HOST = '127.0.0.1'
PORT = 65432

clients = []

def handle_client(cli_soc, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    while True:
        try:
            message = cli_soc.recv(1024).decode('utf-8')
            if message:
                print(f"[{addr}] {message}")
                broadcast(message, cli_soc)
            else:
                remove_client(cli_soc)
                break
        except:
            remove_client(cli_soc)
            break

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                remove_client(client)

def remove_client(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[SERVER STARTED] Listening for connections...")

    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__=="__main__":
    start_server()