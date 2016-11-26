# coding : utf8

import socket

# SCSRC
# Socket Connect Send Recv Close

HOST = '127.0.0.1'
PORT = 666

def connection():

	c = socket.socket()
	c.connect((HOST, PORT))

	message = raw_input(">> ")

	# Taper q pour sortir
	while message != 'q':
		c.send(message)
		c.recv(1024)
		message = raw_input(">> ")

	c.close()

if __name__ == '__main__':
	connection()