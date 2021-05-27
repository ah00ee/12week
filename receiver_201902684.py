import socket
import os
import sys
import hashlib

def check_md5_hash(path):
    f = open(path, 'rb')
    data = f.read()
    md5_hash = hashlib.md5(data).hexdigest()
    return md5_hash

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setblocking(0)
    s.settimeout(15)
    print("receiver socket created")
except socket.error:
    print("failed to create socket")
    sys.exit()

if len(sys.argv) != 3:
    sys.exit()
ip_address = sys.argv[1]
port_number = sys.argv[2]

read = input("enter a command: \n1.receive [file_name]\n2.exit\n")

#
# send to sender
# "receive " + file_name
#

s.sendto(read.encode(), (ip_address, int(port_number)))


if read == "exit":
    sys.exit()

#
# receiver exist msg
#

valid = s.recvfrom(2048)[0]
print(valid.decode('utf-8'))

#
# if receiver exist msg:
#

exist = s.recvfrom(2048)[0]
n = int(s.recvfrom(2048)[0].decode('utf-8'))
print(exist.decode('utf-8'))

#
# file receive ==> open("Received_script.txt", "wb") # Fixed file name
# Receives the standard count for dividing a file from the server
# ==> while recv_count != 0:
# Continuously receive and write file contents
#

f = open("received_file.txt", "wb") 
print("Start receiving file.")
cnt = 0
while n:
    data = s.recvfrom(2048)[0]
    f.write(data)
    cnt += 1
    print("Received packet number:", cnt)
    n -= 1

#
# file_name.close()
#
f.close()

print("Finished receiving file. Check file in directroy.")
