from kivy.clock import Clock
import numpy as np


class Component:
    def __init__(self, inter, name_in):
        self.interaction = inter
        self.actors = {}
        self.name = name_in
        self.current_state = 'idle'
        self.current_action = {}
        self.current_param = None

    def add_transition(self, state, target, fun, value, param=None):
        if state not in self.actors:
            self.actors[state] = {}
        if target not in self.actors[state]:
            self.actors[state][target] = {}
        self.actors[state][target][fun] = (value, param)

    def show(self):
        print(self.name, self.actors)

    def run(self):
        print(self.name, 'running ...')
        Clock.schedule_interval(self.resolve, 0.5)

    def resolve(self, *args):
        # print('resolve', self.name, self.current_state)
        if self.current_state != 'idle':
            called = False
            if self.current_state in self.actors:
                for target,funs in self.actors[self.current_state].items():
                    Q = []
                    for value in funs.values():
                        Q.append(float(value[0]))
                    selected_action = self.select_action(Q)
                    selected_function = funs.keys()[selected_action]
                    selected_param = funs.values()[selected_action][1]
                    self.current_action[target] = [selected_function, selected_param]
                for target,action in self.current_action.items():
                    if action[1] and action[1] == 'x':
                        action[1] = self.current_param
                    self.interaction.components[target].run_function(action)
                    called = True
                self.current_action = {}
            if called:
                self.after_called()

    def after_called(self):
        self.current_state = 'idle'

    def run_function(self, action):
        try:
            if action[1]:
                getattr(self, action[0])(action[1:])
            else:
                getattr(self, action[0])()
            return True
        except:
            print('No function: ', self.name, action)
        return False


    def select_action(self, Q):
        # winner takes all
        return Q.index(max(Q))


