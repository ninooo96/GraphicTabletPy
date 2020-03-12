#Module that contains classes to permit the connection Client-Server
#PyBluez works only with python 3.8.1

 #https://people.csail.mit.edu/albert/bluez-intro/x232.html
import bluetooth
class Connection:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def send(host, port):
