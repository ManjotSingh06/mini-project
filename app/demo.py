from kivy.app import App
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.core.window import Window 

class HomeScreen(Screen):
    pass

class FirstScreen(Screen):
    pass

class MenuScreen(Screen):
    pass

class Manager(ScreenManager):
    pass

class DemoApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        pass
    
DemoApp().run()    