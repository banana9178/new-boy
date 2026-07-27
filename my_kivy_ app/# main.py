# main.py
from kivy.app import App
from kivy.uix.label import Label

class MyFirstApp(App):
    def build(self):
        # 在手机屏幕上显示 "Hello, 我的第一个APP!"
        return Label(text="Hello, 我的第一个APP!")

if __name__ == "__main__":
    MyFirstApp().run()