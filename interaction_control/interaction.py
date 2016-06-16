import json
from component import *


class Interaction:

    def __init__(self):
        self.components = {}
        self.start = None

    def run(self):
        for c in self.components.values():
            c.run()
        print(self.start)
        self.components[self.start[0]].current_state = self.start[1]

    def show(self):
        for c in self.components.values():
            c.show()

    def load(self):
        with open('transitions.json') as data_file:
            data = json.load(data_file)
        for t in data['transitions']:
            info = str(t).split(':')
            source, state, target, fun, value = info[0:5]
            param = None
            if len(info) > 5:
                param = info[5]
            if source not in self.components.keys():
                self.components[source] = Component(self, source)
            if target not in self.components.keys():
                self.components[target] = Component(self, target)
            self.components[source].add_transition(state, target, fun, value, param)
        self.start = data['start'].split(':')
        self.start = [str(x) for x in self.start]
        print("start", self.start)
