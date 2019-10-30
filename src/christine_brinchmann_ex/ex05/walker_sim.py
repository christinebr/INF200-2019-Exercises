# -*- coding: utf-8 -*-
import random

__author__ = "Christine Brinchmann"
__email__ = "christibr@nmbu.no"


class Walker:
    def __init__(self, initial_position, home):
        """
        Parameters
        ----------
        initial_position: the start position
        home: the end position

        Defines number of steps taken as zero.
        """
        self.position = initial_position
        self.home = home
        self.steps = 0

    def move(self):
        """
        Takes a step to the left (-1) or right (+1) from the current position.
        """
        self.steps += 1
        direction = random.uniform(0, 1)
        if direction < 0.5:
            self.position -= 1
        else:
            self.position += 1

    def is_at_home(self):
        """
        Returns True if the end position is reached and False otherwise.
        """
        return self.position == self.home

    def get_position(self):
        """
        Returns the position.
        """
        return self.position

    def get_steps(self):
        """
        Returns number of steps taken.
        """
        return self.steps
