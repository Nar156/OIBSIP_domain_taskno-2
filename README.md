Objective: This project implements a real-time chat application using Python's socket and threading libraries, allowing multiple clients to communicate with each other via a central server over a local network (localhost).

Tools & Libraries Used: Socket - Enables low-level networking and communication Threading - Manages concurrent client connections and input/output

Workflow Server (server.py)

Binds to HOST and PORT and starts listening for connections.
Accepts new clients and starts a thread for each one.
Receives messages from clients and broadcasts them to all other connected clients.
Handles client disconnections gracefully. Client (client.py)
Connects to the server using the same HOST and PORT.
Starts a thread to listen for incoming messages while allowing the user to type and send messages simultaneously.
Sends messages to the server, which are then broadcasted to other clients.
Typing "exit" disconnects the client from the chat.
Sample Output Client 1: [NEW MESSAGE] Hello from client 2 Hi there! Client 2: Hello from client 2 [NEW MESSAGE] Hi there!

How to Run Open two terminals for server and multiple for clients. Start the Server - python server.py Start a Client - python client.py
