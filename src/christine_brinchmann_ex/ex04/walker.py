# -*- coding: utf-8 -*-

__author__ = "Christine Brinchmann"
__email__ = "christibr@nmbu.no"

from random import uniform


class Walker:
    def __init__(self, initial_position, home):
        self.position = initial_position
        self.home = home
        self.steps = 0

    def move(self):
        self.steps += 1
        direction = uniform(0, 1)
        if direction < 0.5:
            self.position -= 1
        else:
            self.position += 1

    def is_at_home(self):
        return self.position == self.home

    def get_position(self):
        return self.position

    def get_steps(self):
        return self.steps
