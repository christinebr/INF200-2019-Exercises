# -*- coding: utf-8 -*-

__author__ = "Christine Brinchmann"
__email__ = "christibr@nmbu.no"

from random import uniform


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
        direction = uniform(0, 1)
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


def walking_process(start_position, distance_home, num_simulations):
    """

    Parameters
    ----------
    start_position: the start position
    distance_home: the distance to the end position
    num_simulations: number of simulations

    Returns
    -------
    num_steps: a list with the steps taken to get from the start position
    to the end position, for each simulation.

    """
    num_steps = []
    for i in range(num_simulations):

        student = Walker(start_position, distance_home)

        while student.is_at_home() is False:
            student.move()

        num_steps.append(student.get_steps())

    return num_steps


if __name__ == '__main__':
    start = 0
    distances = [1, 2, 5, 10, 20, 50, 100]
    num_sim = 5

    steps = []
    for distance in distances:
        steps.append(walking_process(start, distance, num_sim))

    for distance, step in zip(distances, steps):
        sorted_step = sorted(step)
        print('Distance: {0:3d} -> Path lengths: {1}'.format(distance,
                                                             sorted_step))
