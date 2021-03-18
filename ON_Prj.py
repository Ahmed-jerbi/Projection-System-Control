import socket, codecs

#-----------------------
TCP_IP = '192.168.1.137'
TCP_PORT = 1025
MESSAGE = ":POWER1"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE.encode())
#-----------------------

#-----------------------
TCP_IP = '192.168.1.64'
TCP_PORT = 1025
MESSAGE = ":POWER1"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE.encode())
#-----------------------

#-----------------------
TCP_IP = '192.168.1.187'
TCP_PORT = 1025
MESSAGE = ":POWER1"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE.encode())
#-----------------------


#DONE
print("PROJECTORS OFF")