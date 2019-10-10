from random import randint

__author__ = 'Christine Brinchmann', 'Marie Kolvik Valøy'
__email__ = 'christibr@nmbu.no', 'mvaloy@nmbu.no'


ladders_snakes = {
        1: 40,
        8: 10,
        36: 52,
        43: 62,
        49: 79,
        65: 82,
        68: 85,
        24: 5,
        33: 3,
        42: 30,
        56: 37,
        64: 27,
        74: 12,
        87: 70
        }


def single_game(num_players):
    """
    Returns duration of single game.

    Arguments
    ---------
    num_players : int
        Number of players in the game

    Returns
    -------
    num_moves : int
        Number of moves the winning player needed to reach the goal

    Source: https://github.com/yngvem/INF200-2019-Exercises/blob/master
    /exersices/pa01.rst
    """
    positions = [0] * num_players

    num_moves = 0
    while max(positions) < 90:

        for player in range(num_players):

            new_position = positions[player] + randint(1, 6)

            if new_position in ladders_snakes.keys():
                positions[player] = ladders_snakes[new_position]
            else:
                positions[player] = new_position

        num_moves += 1

    return num_moves


def multiple_games(num_games, num_players):
    """
    Returns durations of a number of games.

    Arguments
    ---------
    num_games : int
        Number of games to play
    num_players : int
        Number of players in the game

    Returns
    -------
    num_moves : list
        List with the number of moves needed in each game.

    Source: https://github.com/yngvem/INF200-2019-Exercises/blob/master
    /exersices/pa01.rst
    """


def multi_game_experiment(num_games, num_players, seed):
    """
    Returns durations of a number of games when playing with given seed.

    Arguments
    ---------
    num_games : int
        Number of games to play
    num_players : int
        Number of players in the game
    seed : int
        Seed used to initialise the random number generator

    Returns
    -------
    num_moves : list
        List with the number of moves needed in each game.

    Source: https://github.com/yngvem/INF200-2019-Exercises/blob/master
    /exersices/pa01.rst
    """
