#Module that contains classes to permit the connection Client-Server
#Il modulo PyBluez l'ho installato solo su python 3.8.1

 #https://people.csail.mit.edu/albert/bluez-intro/x232.html
import bluetooth
import sys
class connectionBT:
    """ Class to establish a bluetooth connection Client-Server """
    def __init__(self, host, port):
        self.host = host
        self.port = port
        socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.socket = socket

    def send(self, message):
        self.socket.send(message)
    
    def connect(self):
        self.socket.connect((self.host, self.port))

    def close(self):
        self.socket.close()
    
    #Server Methods. Port must be choose by Server app
    def listen(self):
        self.socket.bind(("", self.port))
        self.socket.listen(1) #accept 1 connection at a time
    
    def accept(self):
        client_socket, address = self.socket.accept()
        return client_socket, address
    
    def receive(self, client_socket):
        data = client_socket.recv(1024)
        print("received", data)
        return data
    
class connectionUtilityBT:
    """ Utility methods for Bluetooth Connection """
    @classmethod
    def searchDevices(cls):
        print ("Search devices...")
        nearby_devices = bluetooth.discover_devices(lookup_names = True)
        print ("Found %d devices" % len(nearby_devices))

        #for name, addr in nearby_devices:
            #print (" %s - %s" % (addr, name))
        return nearby_devices
        
if __name__ == "__main__":
    connectionUtilityBT.searchDevices()