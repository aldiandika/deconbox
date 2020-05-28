import kivy
kivy.require('1.11.1')

from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton

Window.size = (1020, 576)
# Window.fullscreen = True

class HomePage(BoxLayout):
    pass

class HomeApp(MDApp):
    def build(self):
        return HomePage()


if __name__ == '__main__':
    HomeApp().run()