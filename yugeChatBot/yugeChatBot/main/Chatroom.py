# coding: utf-8

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.properties import NumericProperty
from kivy.properties import ListProperty
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.uix.scrollview import ScrollView

from main import YugeChatBot

Window.clearcolor = (0.625, 1, 0.80078, 1)

class Chat(FloatLayout):
    # 縦位置調整
    posY = NumericProperty(0)
    speakerList = ListProperty([])
    mainChatBot = YugeChatBot()

    # run intro
    def startIntro(self):
        

    # display the texts here
    def sentText(self, instance):
        # label position
        self.posY = self.posY+(30/2)
        print(self.posY)

        print("inserted text!")

        # input text
        s = str(self.a.text)
        s = s.replace('\n','')
        print(s)

        # put input text to label
        self.speakerResult.text += 'You: '
        self.speakerResult.text += s
        self.speakerResult.text += '\n'
        self.speakerResult.text += '-----------------------\n'
        self.posY = self.posY+(30/2)

        # get reply

        # senpai's reply
        self.result.text += "野獣先輩: "
        self.result.text += "hahaha\n"
        self.result.text += '-----------------------\n'

    # just for debug
    def reload(self):
        print("Inputbox reloaded")

class TestApp(App):
    icon = 'icon.jpg'
    title = 'ChatBott'

    def build(self):
        self.root = Builder.load_file('root.kv')

        Window.size = (400, 500)
        self.root = Chat()

        return self.root

if __name__ == '__main__':
    TestApp().run()
