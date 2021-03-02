'''
Created on Feb 27, 2021

@author: Administrator
'''
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image

class Mainimage(App):
    def build_image(self):
        wimage = Image(source="C:/Users/Administrator/Desktop/vm_update.png")
        return wimage
if __name__ == '__main__':
    app = Mainimage()
    app.run()
    