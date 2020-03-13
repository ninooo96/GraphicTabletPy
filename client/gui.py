#View of MVC pattern
net=False
bluetooth=False

from kivy.app import App
from kivy.uix.label import label

class Tablet(App):
    def build(self):
        return Label(text="Ciao Antonio")

Tablet().run()