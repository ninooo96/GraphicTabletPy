#View of MVC pattern
from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.textinput import TextInput
from kivy.graphics.vertex_instructions import Rectangle
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
import sys
sys.path.append("C:\\Users\\ninoo\\Documents\\Python project\\Graphic Tablet\\")
import connection as conn
from client import gui


net=False
bluetooth=True
host = ''
port = TextInput(text='')


if(bluetooth):
    utility = conn.connectionUtilityBT
    connection = conn.connectionBT
else:
    #TODO utility = conn.connectionUtilityNET
    #TODO connection = conn.connectionNET
    print("ciao")

 

root = Builder.load_string('''
#:import Window kivy.core.window.Window
FloatLayout:
    canvas.before:
        Color:
            rgba: 1, 1, 1, .2
        Rectangle:
            # self here refers to the widget i.e FloatLayout
            pos: self.pos
            size: self.size   

<BorderLine>:
    canvas:
        Color:
            rgba: 0, 0, 0, .30 
        Rectangle:
            pos: 0.03*Window.width, 0.2*Window.height
            size: 4, 0.6*Window.height
        Rectangle:
            pos: Window.width - 0.03*Window.width-2, 0.2*Window.height
            size: 4, 0.6*Window.height
        Rectangle:
            pos: 0.2*Window.width-1, 0.05*Window.height
            size: 0.6*Window.width, 4
        Rectangle:
            pos: 0.2*Window.width-1, Window.height - 0.05*Window.height
            size: 0.6*Window.width, 4

        
''')

""" search_layout = Builder.load_string('''
BoxLayout:
    canvas.before:
        Color:
            rgba: 1, 1, 1, .2
        Rectangle:
            # self here refers to the widget i.e FloatLayout
            pos: self.pos
            size: self.size   
''') """

class BorderLine(Widget):
    pass

class Home(App):
    def callbackBT(self, istance ):
        App.stop(self)
        SearchBluetooth().run()
        bluetooth = True
        net = False
    
    def callbackNET(self, istance):
        App.stop(self)
        Tablet().run()
        net = True
        bluetooth = False
    
    def build(self):
        Window.size = (300, 150)
        layout = BoxLayout(orientation='horizontal')
    
        bluetooth_btn = Button(background_normal=('bluetooth_logo.png'))
        bluetooth_btn.bind(on_press=self.callbackBT)

        network_btn = Button(background_normal=('wifi_logo.png'))
        network_btn.bind(on_press=self.callbackNET)

        layout.add_widget(bluetooth_btn)
        layout.add_widget(network_btn)
        if(bluetooth):
            utility = conn.connectionUtilityBT
            connection = conn.connectionBT
        else:
            #TODO utility = conn.connectionUtilityNET
            #TODO connection = conn.connectionNET
            print("ciao")
        return layout

class SearchBluetooth(App):
    def callbackBT2(self, instance):
        print(instance.text)
        self.host = instance.text.split(" - ")[1]
        App.stop(self)
        portWindow().run()
        print(instance.text.split(" - ")[1])

    def build(self):
        Window.size = (300, 200)
        layout = BoxLayout(orientation='vertical')
        nearby_devices = utility.searchDevices()
        for device in nearby_devices:
            btn = Button(text=device[1]+" - "+device[0])
            btn.bind(on_press=self.callbackBT2)
            layout.add_widget(btn)
        return layout
        

class portWindow(App):
    def create_connection(self, instance):
        print(port.text)
        """DA ATTIVARE QUANDO LA CONNESSIONE FUNZIONA
        connect = connection(host, int(port.text))
        connect.connect() """
        App.stop(self)
        Tablet().run()

    def build(self):
        Window.size = (300, 30)
        layout = BoxLayout(orientation='horizontal')
        label = Label(text='Port: ')
        button = Button(text='OK', on_press=self.create_connection)
        layout.add_widget(label)
        layout.add_widget(port)
        layout.add_widget(button)
        return layout

class Tablet(App):
    
    def build(self):
        Window.size = (800, 450)
        root.add_widget(BorderLine())
        return root

Home().run()