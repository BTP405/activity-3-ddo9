import pickle
import socket

# Client configuration
HOST = 'localhost'
PORT = 8888

# Function to send tasks to worker nodes
def send_task(task, *args):
    # Pickle the task and its arguments
    task_data = pickle.dumps((task, args))

    # Send the task to the worker node
    client_socket.sendall(task_data)

    # Receive the result from the worker node
    result = client_socket.recv(1024)
    return pickle.loads(result)

# Example task to be executed by the worker nodes
def add(x, y):
    return x + y

if __name__ == "__main__":
    # Create a client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    
    # Send tasks to the worker nodes
    print(send_task(add, 1, 2))  # Output: 3
    print(send_task(add, 3, 4))  # Output: 7

    # Close the client socket
    client_socket.close()
    
    
