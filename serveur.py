# coding : utf8

import socket

# SBLARSC
# Socket Bind Listen Accept Recv Send Close

HOST = '127.0.0.1'
PORT = 666

def connection():

	s = socket.socket()
	s.bind((HOST, PORT))
	s.listen(1)
	c, addr = s.accept()

	while True:
		data = c.recv(1024)
		if not data:
			break
		print ">> " + str(data)

		c.send(data)

	s.close()

if __name__ == '__main__':
	connection()
