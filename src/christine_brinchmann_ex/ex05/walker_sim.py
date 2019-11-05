# -*- coding: utf-8 -*-
import random

__author__ = "Christine Brinchmann"
__email__ = "christibr@nmbu.no"


class Walker:
    def __init__(self, initial_position, home):
        """
        Parameters
        ----------
        initial_position: the initial position of the walker
        home: the position of the walker's home

        Defines number of steps taken as zero.
        """
        self.position = initial_position
        self.home = home
        self.steps = 0

    def move(self):
        """
        Takes a step to the left (-1) or right (+1) from the current position,
        with equal probability.
        """
        self.steps += 1
        direction = random.uniform(0, 1)
        if direction < 0.5:
            self.position -= 1
        else:
            self.position += 1

    def is_at_home(self):
        """Returns True if the walker is at home and False otherwise."""
        return self.position == self.home

    def get_position(self):
        """Returns the current position."""
        return self.position

    def get_steps(self):
        """Returns number of steps taken by the walker."""
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


if __name__ == '__main__':
    seeds = [12345, 12345, 54321]
    sim_steps_1 = []
    sim_steps_2 = []
    for i in range(len(seeds)):
        sim_walk_1 = Simulation(0, 10, seeds[i])  # from start 0 to home 10
        sim_walk_2 = Simulation(10, 0, seeds[i])  # from start 10 to home 0

        sim_steps_1.append(sim_walk_1.run_simulation(20))  # 20 walks
        sim_steps_2.append(sim_walk_2.run_simulation(20))  # 20 walks

    print('20 walks from start 0 to home 10:')
    for step1, seed_value in zip(sim_steps_1, seeds):
        sorted_step1 = sorted(step1)

        print('seed: {0} --> Number of steps: {1}'.format(seed_value,
                                                          sorted_step1))

    print('\n20 walks from start 10 to home 0:')
    for step2, seed_value in zip(sim_steps_2, seeds):
        sorted_step2 = sorted(step2)
        print('seed: {0} --> Number of steps: {1}'.format(seed_value,
                                                          sorted_step2))
