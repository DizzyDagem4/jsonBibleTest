import json
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import DictProperty
from kivy.uix.screenmanager import ScreenManager, Screen
class Bible(Screen):
    data = DictProperty({})
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with open("amharic_bible.json", "r",encoding="utf-8") as f:
            self.data = json.load(f)
class MyWidget(BoxLayout):
    pass

class MyApp(App):
    def build(self):
        Builder.load_file("GUI.kv")
        sm = ScreenManager()
        sm.add_widget(Bible(name='bible'))
        return sm
        return MyWidget()

if __name__ == "__main__":
    MyApp().run()
