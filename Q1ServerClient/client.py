import socket
import pickle

def runClient():
    file_path = "./Q1ServerClient/file_to_send.txt"

    try:
        with open(file_path, "rb") as file:
                    data = file.read()
                    file_data= {
                        "filename": file_path.split("/")[-1],
                        "data": data
                    }

        pickled_data = pickle.dumps(file_data)
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((socket.gethostname(), 1234))
        s.sendall(pickled_data)
        print("Client: File sent successfully.")
    except Exception as e:
        print(f"Client: Error sending file: {e}")