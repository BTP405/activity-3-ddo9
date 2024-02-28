import pickle
import socket
import threading
from client import add

# Worker function to execute tasks
def worker(connection):
    while True:
        try:
            # Receive the task (pickled function and arguments)
            task_data = connection.recv(1024)
            if not task_data:
                break
            task, args = pickle.loads(task_data)

            # Execute the task
            result = task(*args)

            # Send the result back to the client
            connection.send(pickle.dumps(result))
        except Exception as e:
            print(f"Worker error: {e}")
            break

# Server configuration
HOST = 'localhost'
PORT = 8888

# Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print("Worker node started.")

while True:
    # Accept incoming connections from the client
    connection, address = server_socket.accept()
    print(f"Connected to {address}")

    # Start a new thread to handle the client request
    threading.Thread(target=worker, args=(connection,)).start()
