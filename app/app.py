from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import BoxLayout
from kivy_garden.mapview import MapView,MapMarker
from kivymd.uix.selectioncontrol import MDCheckbox
from kivy.properties import StringProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import requests



class HomeScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class MapScreen(Screen):
    pass


class ReportScreen(Screen):
    def submit_form(self):
        # Collect the data from the inputs (using self.ids)
        name = self.ids.name_input.text
        phone = self.ids.phone_input.text
        location = self.ids.location_input.text
        time = self.ids.time_input.text
        vehicle_details = self.ids.vehicle_details_input.text
        emergency_contact = self.ids.emergency_contact_input.text

        # Basic validation for required fields
        if not name or not phone or not location or not time:
            self.show_error_popup("Please fill out all required fields.")
            return
        
        # Prepare the data to be sent
        form_data = {
            'name': name,
            'phone': phone,
            'location': location,
            'time': time,
            'vehicle_details': vehicle_details,
            'emergency_contact': emergency_contact
        }

        
        url = "http://127.0.0.1:5000/notify-hospital"  # Flask server URL


        try:
            # Send POST request to the Flask server
            response = requests.post(url, json=form_data)

            # Check if the request was successful
            if response.status_code == 200:
                self.show_confirmation_popup("Alert sent to nearby hospital successfully!")
            else:
                self.show_error_popup(f"Failed to send alert. {response.json().get('error')}")
        except requests.exceptions.RequestException as e:
            # Handle errors in case the request fails
            self.show_error_popup(f"Error: {e}")


    def show_error_popup(self, message):
        # Error popup if the required fields are not filled
        popup = Popup(title="Error", content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()


    def show_confirmation_popup(self, message):
        # Confirmation popup when the form is successfully submitted
        popup = Popup(title="Confirmation", content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()



class Manager(ScreenManager):
    pass



class MainApp(MDApp):
    '''def CheckItem(MDBoxLayout):
        text = StringProperty()
        group = StringProperty()'''


    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"
        return Builder.load_file('app.kv')
    
    
    def logger(self):
        username = self.root.get_screen('login').ids.user.text
        password = self.root.get_screen('login').ids.password.text
        self.root.get_screen('login').ids.welcome_label.text=f'WELCOME {username} !'
    
    
    
    def set_marker(self):
        # Getting the MapView widget by its ID 
        map_view = self.root.ids.map.ids.map_view

        # Setting a marker at the hospital location,
        new_marker = MapMarker(lat=28.4737187, lon=77.48358)  # sharda college 
        map_view.add_marker(new_marker)
    
    

    
    def clear(self):
        self.root.get_screen('login').ids.welcome_label.text='WELCOME'
        self.root.get_screen('login').ids.user.text=''
        self.root.get_screen('login').ids.password.text=''

MainApp().run()