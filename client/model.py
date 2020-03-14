import sys
sys.path.append("C:\\Users\\ninoo\\Documents\\Python project\\Graphic Tablet\\client\\")
import connection as conn
import gui

if(gui.bluetooth):
    utility = conn.connectionUtilityBT
    connection = conn.connectionBT
else:
    #TODO utility = conn.connectionUtilityNET
    #TODO connection = conn.connectionNET
    print("ciao")

