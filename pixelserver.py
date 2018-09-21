#!/usr/bin/python         

import SocketServer

class MyTCPHandler(SocketServer.BaseRequestHandler):
    message = ""

    def handle(self):
        # self.request: TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        self.request.sendall(MyTCPHandler.message)

if __name__ == "__main__":
    HOST, PORT = "", 80
    
    f = open("/opt/pixelserver/1pixel.png", "rb")
    contents = f.read()
    f.close()

    MyTCPHandler.message = "HTTP/1.1 200 OK\r\nContent-type: image/gif\r\nAccept-ranges: bytes\r\nContent-length: " \
        + str(len(contents)) + "\r\n\r\n"
	+ "Connection: close\r\n" \
	+ str(len(contents)) + "\r\n\r\n" + contents + "\r\n\r\n"

    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    
    # Start the server
    server.serve_forever()
