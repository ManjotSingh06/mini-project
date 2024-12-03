from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from plyer import gps

class GPSApp(App):
    def build(self):
        self.label = Label(text="Press the button to get GPS location", size_hint=(None, None), size=(400, 200))
        button = Button(text="Get GPS Location", size_hint=(None, None), size=(200, 100))
        button.bind(on_press=self.get_gps_location)
        return button

    def get_gps_location(self, instance):
        # Start the GPS service to get location
        gps.configure(on_location=self.on_location)
        gps.start()

    def on_location(self, **kwargs):
        # Extract the latitude and longitude from the callback
        latitude = kwargs.get('lat', 'Unknown')
        longitude = kwargs.get('lon', 'Unknown')

        # Update the label with the location
        self.label.text = f"Latitude: {latitude}\nLongitude: {longitude}"

    def on_stop(self):
        # Stop the GPS service when the app is closed
        gps.stop()

if __name__ == '__main__':
    GPSApp().run()
