from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

Window.clearcolor = (0.625, 1, 0.80078, 1)

Builder.load_string("""
<Calc>:
    # This are attributes of the class Calc now
    a: _a
    result: _result
    speakerResult: _speakerResult

    #String代入
    # _speakerResult.text = str("hohoho")

    ScreenManager:
        size_hint: 1, 1.0
        id: _screen_manager
        Screen:
            name: 'screen1'
            GridLayout:
                # cols:2
                Label:
                    id: _result
                    color: 1,0,1,1
                    center_x: (root.width/4)
                    center_y: (400)
                Label:
                    id: _speakerResult
                    color: 1,0,1,1
                    center_x: (root.width/4*3)
                    center_y: (400)

                TextInput:
                    id: _a
                    # text: '3'
                    hint_text: "Let's talk!"
                    font_size: 30
                    x: (20)
                    center_y: (200)
                    size: 600,70
                # Label:
                #     id: _result

                Button:
                    font_size: 50
                    center_x: (root.width-80)
                    center_y: (200)
                    size: 130,70
                    # top: root.top-180
                    text: 'send'
                    # Or you can call a method from the root class (instance of calc)
                    # on_press: root.product(*args)
                    on_press: root.sentText(*args)

        Screen:
            name: 'screen2'
            Label:
                text: 'The second screen'
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'bottom'
        BoxLayout:
            orientation: 'horizontal'
            size_hint: 1, .1
            Button:
                text: 'Go to Screen 1'
                on_press: _screen_manager.current = 'screen1'
            Button:
                text: 'Go to Screen 2'
                on_press: _screen_manager.current = 'screen2'
                """)

class Calc(FloatLayout):
    # define the multiplication of a function
    def product(self, instance):
        # self.result, self.a and self.b where defined explicitely in the kv
        self.result.text = str(int(self.a.text) * int(self.a.text))

    def sentText(self, instance):
        self.speakerResult.text += str(self.a.text+"\n")

class TestApp(App):
    def build(self):
        Window.size = (400, 500)
        root = Calc()
        return root

if __name__ == '__main__':
    TestApp().run()
