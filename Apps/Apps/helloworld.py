'''
Created on Feb 25, 2021

@author: Administrator
'''
import kivy
from kivy.app import App
from kivy.uix.label import Label

class Myapp(App):
    def build(self):
        return Label(text="Hello world")

    
if __name__ == '__main__':
    app = Myapp()
    app.run()
