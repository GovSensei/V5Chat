# Imports
import socket
import threading
import time
import sys

# Server
host = socket.gethostbyname(socket.gethostname())
port = 5050
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
addr = (server, port)
server.bind(addr)

# Client handler
def client_handler(conn, addr):
    pass

# Start
def start_server():
    pass