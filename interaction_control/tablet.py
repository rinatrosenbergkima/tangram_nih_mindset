from component import *


class TabletComponent(Component):
    def first_screen(self):
        print(self.name, 'first_screen')
        self.current_state = 'first_screen'

    def yes(self):
        print(self.name, 'yes')
        self.current_state = 'yes'

    def wait(self):
        print(self.name, 'wait')
        self.current_state = 'wait'

    def selection_screen(self, x):
        print(self.name, 'selection_screen', x)
        self.current_state = 'selection_screen'

    def tangram_screen(self, x):
        print(self.name, 'tangram_screen', x)
        self.current_state = 'tangram_screen'

    def hourglass_update(self, x):
        print(self.name, 'hourglass update', x)
