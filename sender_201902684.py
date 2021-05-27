import socket
import os
import sys
import hashlib
'''
if len(sys.argv) != 2:
    print("Fail! - Require two arguments.")
    sys.exit()
port = sys.argv[1]
'''
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", int(8111)))
    print('바보')
except socket.error:
	print("failed to create socket")
	sys.exit()

def check_md5(path):
	f = open(path, 'rb')
	data = f.read()
	md5_hash = hashlib.md5(data).hexdigest()
	return md5_hash

def sender_send(file_name):
    # 4-a
    sock.sendto("valid list command.".encode('utf-8'), addr)
    # 4-b
    if os.path.isfile(file_name):
        # 4-c
        size = os.stat(file_name).st_size
        n, cnt = int(size/2048), 0
        sock.sendto("file exists!".encode('utf-8'), addr)
        sock.sendto(str(n).encode('utf-8'), addr)

        read_file = open(file_name, "rb") # read for bytes
        print("Start sending file.")

        # 4-d
        while n:
            r = read_file.read(2048)
            sock.sendto(r, addr)
            cnt += 1
            print("packet number:", cnt)
            n -= 1
        print("Finished sending file.")

    else:
        sock.sendto("filt not exists!".encode('utf-8'), addr)

try:
    data, addr = sock.recvfrom(2048)
    data = data.decode()
except ConnectionResetError:
    print("error. port number not matching.")
    sys.exit()

handler = data.split()

if handler[0] == 'receive':
    sender_send(handler[1])
else:
    print("exit")
    sock.close()
    sys.exit()