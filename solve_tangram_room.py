from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import Layout
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.clock import Clock
from kivy.app import App
from kivy.animation import Animation
from kivy.core.window import Window

Builder.load_string('''
<RootWidget>:
    Background:
        size: root.size
        pos: root.pos
    TreasureBox:
        size: root.size
        pos: root.pos
    HourGlassWidget:
        id: hourglass

<Background>:
    Image:
        size: root.size
        pos: root.pos
        source: 'images\Tangram_background.jpg'
        allow_stretch: True
        keep_ratio: False

<TreasureBox>:
    Image:
        id: box
        size: root.width * 0.6, root.height * 0.6
        pos: root.width * 0.2, root.height * 0.2
        source: 'images\TreasureBoxLayers.gif'
        allow_stretch: True
        keep_ratio: False

    Image:
        id: rotate
        size: root.width * 0.08, root.height * 0.1
        pos: root.width * 0.65, root.height * 0.48
        source: 'images\Tangram_rotate_btn.gif'
        allow_stretch: True
        keep_ratio: False
        on_touch_down: root.rotate_shape()

<HourGlassWidget>:
    Image:
        id:topSand
        source: 'images\sand.jpg'
        allow_stretch: True
        keep_ratio: False
    Image:
        id:middleSand
        source: 'images\sand.jpg'
        allow_stretch: True
        keep_ratio: False
    Image:
        id:bottomSand
        source: 'images\sand.jpg'
        allow_stretch: True
        keep_ratio: False
    Image:
        id: hourglass
        source: 'images\hour_glass.gif'
        allow_stretch: True
        keep_ratio: False
        pos: self.pos
        size: self.size
''')


class RootWidget(Widget):
    pass


class Background(Widget):
    pass


class TreasureBox(Widget):
    def rotate_shape(self, *kwargs):
        print("rotate shape")


class HourGlassWidget (Widget):
    def __init__(self, **kwargs):
        super(HourGlassWidget, self).__init__(**kwargs)
        self.delta=0
        #self.animate_sand()
        Clock.schedule_interval(self.after_init,0.01)  #only after init is done ids can be accessed

    def after_init(self, *args):
        self.hourglass = self.ids['hourglass']
        self.topSand = self.ids['topSand']
        self.middleSand = self.ids['middleSand']
        self.bottomSand = self.ids['bottomSand']
        self.init = False
        self.do_layout()
        self.start_hourglass(120)
        return False


    def do_layout(self, *args):
        if (not self.init):
            self.size = Window.width * 0.08, Window.height * 0.2
            self.pos = Window.width * 0.85, Window.height * 0.25
            self.delta = (self.height * 0.2) / 60.0
            sandWidth = self.width
            sandHeight = self.height * 0.25
            self.delta = sandHeight / 480.0   #120*4
            self.hourglass.size = self.width, self.height
            self.hourglass.pos = self.x, self.y
            self.topSand.size = sandWidth, sandHeight
            self.topSand.pos = self.x, self.y+self.height * 0.5
            self.middleSand.size = sandWidth * 0.05, sandHeight * 2
            self.middleSand.pos = self.x + sandWidth/2.0 - sandWidth*0.02, self.y+0
            self.bottomSand.size = sandWidth, 0
            self.bottomSand.pos = self.x, self.y+0 + self.height * 0.039
            self.init = True


    def start_hourglass (self, seconds):
        self.counter = seconds * 4 #for 4 ticks per second
        Clock.schedule_interval(self.update_hourglass, 0.25)

    def finish_hourglass(self, *args):
        self.middleSand.height = 0
        print("time is up")

    def update_hourglass (self, *args):
        print("update ", self.counter)
        self.topSand.height = self.topSand.height - self.delta
        self.bottomSand.height = self.bottomSand.height + self.delta
        self.counter -= 1
        if self.counter <= 0:
            self.finish_hourglass()
            return False
        return True

    def animate_sand (self,*args):
        animTop = Animation(height=0,
                         duration=60,
                         transition='in_quad')
        #animTop.start(self.topSand)
        animBottom = Animation(height=100,
                         duration=4,
                         transition='in_quad')
        animBottom.start(self.bottomSand)


# runTouchApp(RootWidget())

class RootWidgetApp(App):
    def build(self):
        rw = RootWidget()
        print(rw.ids['hourglass'])
        return rw

if __name__ == "__main__":
    RootWidgetApp().run()
