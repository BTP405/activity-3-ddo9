import socket
import pickle

def runServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 1234))
    s.listen(5)
    print("Server: Waiting for connection...")

    clientsocket, address = s.accept()
    print("Server: Connection established.")

    try:
        pickled_data = clientsocket.recv(4096)
        file_data = pickle.loads(pickled_data)
        
        file_path = "./Q1ServerClient/received_files" + "/" + file_data["filename"]
        with open(file_path, 'wb') as file:
            file.write(file_data["data"])
            
        print(f"Server: File received and saved to {file_path}.")
    except Exception as e:
        print(f"Server: Error receiving file: {e}")

    clientsocket.close()    