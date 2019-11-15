# -*- coding: utf-8 -*-
import random

__author__ = 'Christine Brinchmann', 'Marie Kolvik Valøy'
__email__ = 'christibr@nmbu.no', 'mvaloy@nmbu.no'

import src.pa02.chutes_simulations as ss


class TestPBoard2:
    """Tests that Board works as supposed."""

    def test_goal_reached(self):
        """
        Check that goal is not reached when the position is 5 and the goal is
        at position 100
        """
        board = ss.Board(goal=100)
        assert board.goal_reached(5) is False

    def test_position_adjustment(self):
        """
        Checks that position_adjustment returns the correct number of steps
        to be subtracted or added when the position is on the top of a snake
        or the bottom of a ladder. Checks that position_adjustment returns 0
        when the position is elsewhere.
        """
        board = ss.Board()
        assert board.position_adjustment(8) == 10-8

        assert board.position_adjustment(56) == 37-56

        assert board.position_adjustment(63) == 0


class TestPlayer2:
    """Tests that Player works as supposed."""

    def test_move_original(self):
        """
        Checks that:
         *the start position is zero
         *the player have moved after move() is called
         *the player cant be at the bottom of a ladder
         *the player cant be at the top of a snake
        """
        player = ss.Player()
        assert player.position == 0, 'Start position is not 0'
        random.seed(2)
        player.move()
        assert player.position > 0, 'The player has not moved'
        assert player.position != 1, 'The player cant be at the bottom of a ' \
                                     'ladder'
        random.seed(1)
        player.move()
        assert player.position != 42, 'The player cant be at the top of a ' \
                                      'snake'


class TestResilientPlayer2:
    """Tests that ResilientPlayer works as supposed."""
    def test_move_default_extra_steps(self):
        """
        Test that ResilientPlayer takes one extra step after sliding
        down a snake

        First move: 1 -> goes up ladder to position 40
        Second move: 2 -> goes down snake to position 30
        Third move: 1 -> should add the extra steps and end up at position 32
        """
        player = ss.ResilientPlayer()
        random.seed(2)
        player.move()
        random.seed(1)
        player.move()
        random.seed(2)
        player.move()
        assert player.position == 32


class TestLazyPlayer2:
    """Tests that LazyPlayer works as supposed."""
    def test_move_default_dropped_steps(self):
        """
        Test that LazyPlayer takes one step less after going up a ladders.

        First move: 1 -> goes up ladder to position 40
        Second move: 5 -> should drop 1 step and end up at 44
        """
        player = ss.LazyPlayer()
        random.seed(2)
        player.move()
        random.seed(5)
        player.move()
        assert player.position == 44

    def test_move_dropped_steps_greater_than_move(self):
        """
        Tests that LazyPlayer dont move backwards when dropped steps are
        greater than the next move

        First move: 1 -> goes up ladder to position 40
        Second move: 1 -> should not move because dropped_steps > move
        """
        player = ss.LazyPlayer(dropped_steps=3)
        random.seed(2)
        player.move()
        random.seed(2)
        player.move()
        assert player.position == 40


class TestSimulaiton2:
    """Tests the class Simulation"""

    def test_single_game_returns_tuple(self):
        """Tests that single_game returns a tuple."""
        sim = ss.Simulation()
        assert type(sim.single_game()) == tuple, 'single_game should return ' \
                                                 'tuple'

    def test_single_game_works(self):
        """
        Tests that two games of single_game is different from each other.
        """
        sim = ss.Simulation()
        game1 = sim.single_game()
        game2 = sim.single_game()
        assert game1 != game2, 'Your method single_game is not working.'

    def test_run_simulation_returns_nothing(self):
        """Tests that run_simulation returns nothing"""
        sim = ss.Simulation()
        assert sim.run_simulation(10) is None

    def test_run_simulation_stores_result(self):
        """Tests that run_simulation stores the results"""
        sim = ss.Simulation()
        assert sim.results == []
        sim.run_simulation(10)
        assert sim.results != []

    def test_get_results_returns_list_of_tuples(self):
        """Tests that get_results returns a list consisting of tuples."""
        sim = ss.Simulation()
        sim.run_simulation(5)
        assert type(sim.get_results()) == list
        assert type(sim.get_results()[0]) == tuple

    def test_get_results_returns_all_results(self):
        """
        Tests that get_results contains the same number of winners as
        games played.
        """
        sim = ss.Simulation()
        sim.run_simulation(7)
        assert len(sim.get_results()) == 7

    def test_winners_per_type_returns_dict(self):
        """Tests that winners_per_type returns a dictionary"""
        sim = ss.Simulation()
        assert type(sim.winners_per_type()) == dict

    def test_winners_per_type_num_players(self):
        """Tests that all types of players are present"""
        type_of_player = ['Player', 'LazyPlayer', 'ResilientPlayer']
        sim = ss.Simulation()
        run = sim.winners_per_type()
        assert list(run.keys()) == type_of_player

    def test_winners_per_type_sum(self):
        """Tests that total wins are equal to numbers of simulation."""
        sim = ss.Simulation()
        sim.run_simulation(14)
        winners = sim.winners_per_type()
        assert sum(winners.values()) == 14

    def test_durations_per_type(self):
        """Tests that durations_per_type returns a dictionary"""
        sim = ss.Simulation()
        assert type(sim.durations_per_type()) == dict

    def test_durations_per_type_num_players(self):
        """Tests that all types of players are present"""
        type_of_player = ['Player', 'LazyPlayer', 'ResilientPlayer']
        sim = ss.Simulation()
        run = sim.durations_per_type()
        assert list(run.keys()) == type_of_player

    def test_players_per_type(self):
        """Tests that players_per_type returns dictionary"""
        sim = ss.Simulation()
        assert type(sim.players_per_type()) == dict

    def test_players_per_type_num_players(self):
        """Tests that all types of players are present"""
        type_of_player = ['Player', 'LazyPlayer', 'ResilientPlayer']
        sim = ss.Simulation()
        run = sim.players_per_type()
        assert list(run.keys()) == type_of_player
