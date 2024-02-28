import socket
import pickle
import threading

def readMsg():
    while True:
        try:
            if s:
                pickled_msg = s.recv(1024)
                recvMsg = pickle.loads(pickled_msg)
                print(recvMsg)
            else:
                break
        except Exception as e:
            print(f"Client: Receiving sending message: {e}")
            break
            
def sendMsg():
    while True:
        sendingMsg = input("") 
        
        pickled_data = pickle.dumps(sendingMsg)
        s.sendall(pickled_data)
        
        if sendingMsg == "[q]":
            break
            
    
def runClient():
    
    threading.Thread(target=readMsg).start()
    
    threading.Thread(target=sendMsg).start()
    
        
if __name__ == "__main__":
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1234))
    
    print("Welcome to the chat.")
    print("Enter [q] anytime to leave the chat.")
    
    runClient()