from kivymd.app import MDApp
from kivymd.uix.boxlayout import BoxLayout
from kivy_garden.xcamera import XCamera  # Install this for mobile
from kivy.uix.webview import WebView  # Install kivy-garden-webview

class MapApp(MDApp):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Load the Google Map HTML file
        self.webview = WebView(url='map.html')
        layout.add_widget(self.webview)

        return layout

if __name__ == '__main__':
    MapApp().run()
