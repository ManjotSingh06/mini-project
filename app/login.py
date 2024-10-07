from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window 

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        
        # Create layout
        self.orientation = 'vertical'
        self.spacing = 50
        self.padding = 200
        
        
        # Username input
        self.username_input = TextInput(hint_text='Username',
                                         multiline=False,
                                         size_hint=(None,None),
                                         size=(400,200),
                                         pos_hint={'center_x':.5,'center_y':.5},
                                         background_color =(1,0,0,0.9),

                                         )
        self.add_widget(self.username_input)
        
        # Password input
        self.password_input = TextInput(hint_text='Password',
                                         password=True,
                                           multiline=False,
                                           size_hint=(None,None),
                                           size=(400,200),
                                           pos_hint={'center_x':0.5,'center_y':0.5},
                                           background_color =(1,0,0,0.9)
                                           )
        self.add_widget(self.password_input)
        
        # Login button
        self.login_button = Button(text='Login',
                                   size_hint=(None,None),
                                   size=(250,200),
                                   pos_hint={'center_x':0.5,'center_y':0.5}
                                   )
        self.login_button.bind(on_press=self.validate_login)
        self.add_widget(self.login_button)

    def validate_login(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        
        # Simple validation (replace with your own logic)
        if username == "admin" and password == "password":
            self.show_popup("Success", "Login Successful!")
        else:
            self.show_popup("Error", "Invalid Username or Password.")

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.6, 0.4))
        popup.open()

class MyApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()
