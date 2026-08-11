from kivy.app import App
from kivy.uix.label import Label

class ArhAIApp(App):
    def build(self):
        return Label(text='Hello! ARH AI App is Connected Successfully!', font_size=24)

if __name__ == '__main__':
    ArhAIApp().run()
