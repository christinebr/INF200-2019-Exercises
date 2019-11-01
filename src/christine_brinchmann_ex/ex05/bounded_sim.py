# -*- coding: utf-8 -*-

from src.christine_brinchmann_ex.ex05.walker_sim import Walker, Simulation

__author__ = "Christine Brinchmann"
__email__ = "christibr@nmbu.no"


class BoundedWalker(Walker):
    def __init__(self, start, home, left_limit, right_limit):
        """
        Initialise the walker

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        super().__init__(start, home)
        self.left_limit = left_limit
        self.right_limit = right_limit

    def move(self):
        """
        Takes a step to the left (-1) or right (+1) from the current position,
        with equal probability. If the walker goes beyond the left_limit or
        the right_limit, the walker's position is set to that limit.
        """
        super().move()

        if self.position < self.left_limit:
            self.position = self.left_limit

        if self.position > self.right_limit:
            self.position = self.right_limit


class BoundedSimulation(Simulation):
    def __init__(self, start, home, seed, left_limit, right_limit):
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
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        super().__init__(start, home, seed)
        self.left_limit = left_limit
        self.right_limit = right_limit

    def single_walk(self):
        """
        Simulate single walk from start to home, returning number of steps.

        Returns
        -------
        int
            The number of steps taken
        """
        bounded_walker = BoundedWalker(self.start, self.home, self.left_limit,
                                       self.right_limit)

        while not bounded_walker.is_at_home():
            bounded_walker.move()

        return bounded_walker.get_steps()
