from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from androidstorage4kivy import Chooser
from android.permissions import Permission

class UI(BoxLayout):
    def __init__(self, **kwargs):
        super(UI, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 20
        self.chooser = Chooser(self.chooser_callback)
        label = Label(text="[b]file chooser[/b]", markup=True, size_hint=(1,.2))
        laber1 = Label(text="file paths", size_hint=(1,.2))
        image = Image(source="", size_hint=(1,.6), pos_hint={'center_x': .5})
        button = Button(text="choose file", on_pess=self.select, size_hint=(.6,.2), pos_hint={'center_x': .5})

        self.add_widget(label)
        self.add_widget(laber1)
        self.add_widget(image)
        self.add_widget(button)
    
    def select(self, *args):
        self.chooser.choose_content("image/*")

    def chooser_callback(self, path):
        self.label1.text = path
        self.image.source = path

class Main(App):
    def build(self):
        return UI()
    def on_start(self):
        self.permissions = [Permission.READ_MEDIA_IMAGES]
    
Main().run()
