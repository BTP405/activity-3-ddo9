import socket
import threading
import pickle

clients = []

def handleClient(client_socket, address):
    print(f"Server: Connection established with {address}")
    
    clients.append(client_socket)
    
    for c in clients:
        if c != client_socket:
            pickled_msg = pickle.dumps(f"Client {address} has connected to the chat.")
            c.sendall(pickled_msg)
            # c.sendall(bytes(f"Client {address} has connected to the chat.", "utf-8"))
        
    while True:
        try:
            pickled_data = client_socket.recv(1024)
            if not pickled_data:
                break
            
            message = pickle.loads(pickled_data)
            
            if message == "[q]":
                break
            
            for c in clients:
                pickled_msg = pickle.dumps(f"Client {address}: {message}")
                c.sendall(pickled_msg)
                # c.sendall(bytes(f"Client {address}: {message}", "utf-8"))
        except Exception as e:
            print(f"Server: Error receiving message: {e}")
            break
    
    clients.remove(client_socket)
    client_socket.close()
    print(f"Client {address} has disconnected from the chat.")
    
def runServer():
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 1234))
    s.listen()
    print("Chat Server Started.")

    while True:
        client_socket, address = s.accept()

        threading.Thread(target=handleClient, args=(client_socket, address)).start()
        
if __name__ == "__main__":
    runServer()