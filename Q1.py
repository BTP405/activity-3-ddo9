#Implement a client-server file transfer application where the client sends a file to the server using sockets. 
#Before transmitting the file, pickle the file object on the client side. On the server side, receive the pickled file object, unpickle it, and save it to disk.


#Requirements:
#The client should provide the file path of the file to be transferred.
#The server should specify the directory where the received file will be saved.
#Ensure error handling for file I/O operations, socket connections, and pickling/unpickling.

import threading
from Q1ServerClient.server import runServer
from Q1ServerClient.client import runClient

if __name__ == "__main__":
    
    stream_lock = threading.Lock()
    
    t_server = threading.Thread(target=runServer).start()
    t_client = threading.Thread(target=runClient).start()