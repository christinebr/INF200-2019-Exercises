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


class Simulation:
    def __init__(self, start, home, seed):
        """
        Initialise the simulation

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        seed : int
            Random generator seed
        """
        self.start = start
        self.home = home
        random.seed(seed)

    def single_walk(self):
        """
        Simulate single walk from start to home, returning number of steps.

        Returns
        -------
        int
            The number of steps taken
        """
        walker = Walker(self.start, self.home)

        while not walker.is_at_home():
            walker.move()

        return walker.get_steps()

    def run_simulation(self, num_walks):
        """
        Run a set of walks, returns list of number of steps taken.

        Arguments
        ---------
        num_walks : int
            The number of walks to simulate

        Returns
        -------
        list[int]
            List with the number of steps per walk
        """
        num_steps = []
        for walk in range(num_walks):
            num_steps.append(self.single_walk())

        return num_steps
