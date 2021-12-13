#TCP server listener to control windows tasks remotely
#developed under python v3.9.5

import socket
import os


# Init
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Set the client TCP port
port = 5005
sock.bind(('', port))
sock.listen(2)
print ("Listening to port", port , "...")

# loop waiting for messages (terminate with Ctrl-C or closing the console)
try:
    while 1:
        newSocket, address = sock.accept(  )
        while 1:
            rawReceivedData = newSocket.recv(1024)
            if not rawReceivedData: break
            # ------- MESSAGE HANDLING --------
            # Decode byte to str (utf8)
            receivedMsg = rawReceivedData.decode("UTF-8")
            print ("Client ", address, "--> RECEIVED MESSSAGE:", receivedMsg)
            
            #check content for actions: watch out for special characters and carriage returns
            if receivedMsg == 'start\n': 
                print ("-ACTION 1 -")
                #start a task. The file can also be a .bat for complex operations
                os.startfile('"C:\Your_App_Name.exe"')
            elif receivedMsg == 'stop\n':
                print("-ACTION 2 -")
                #kill a task
                os.system("taskkill /f /im  Your_Process_Name.exe")
            
            # Optional: Echo back the client
            newSocket.send(rawReceivedData)
            # ------- END of MESSAGE HANDLING  -------
        newSocket.close(  )
finally:
    sock.close(  )