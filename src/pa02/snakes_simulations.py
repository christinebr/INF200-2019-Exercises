# -*- coding: utf-8 -*-

__author__ = 'Christine Brinchmann', 'Marie Kolvik Valøy'
__email__ = 'christibr@nmbu.no', 'mvaloy@nmbu.no'


class Board:
    """
    Creates a standard board for the snakes and ladders game if not specified
    """

    def __init__(self,
                 ladders=((1, 40), (8, 10), (36, 52), (43, 62), (49, 79),
                          (65, 82), (68, 85)),
                 chutes=((24, 5), (33, 3), (42, 30), (56, 37), (64, 27),
                         (74, 12), (87, 70)),
                 goal=90):
        self.ladders = ladders
        self.chutes = chutes
        self.goal = goal

    def goal_reached(self, position):
        """ Return True if the goal is reached"""
        return True

    def position_adjustment(self, position):
        """

        Parameters
        ----------
        position:
            the position of the player

        Returns
        -------
        0:
            if player not at the start of a snake or ladder
        num_step:
            number of position the player must move forward or backward due to
            a ladder or a snake

        """
        return 0


class Player:
    def __init__(self, board=Board()):
        self.board = board

    def move(self):
        pass


class ResilientPlayer(Player):
    def __init__(self):
        super().__init__()
        pass


class LazyPlayer(Player):
    def __init__(self):
        super().__init__()
        pass


class Simulation:
    def __init__(self):
        pass
