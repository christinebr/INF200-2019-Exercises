
from random import randint as random_integer

__author__ = 'Christine Brinchmann'
__email__ = 'christibr@nmbu.no'


def one_guess():
    """ Asks for a number between 2 and 12, and converts the input to an
    integer
    """
    guess = 0
    while guess < 2 or guess > 12:
        guess = int(input('Please guess a number between 2 and 12: '))
    return guess


def random_number():
    """ Generates a random number between 2 and 12 """
    return random_integer(1, 6) + random_integer(1, 6)


def check_guess(correct_answer, guess):
    """ Checks if the guess given is correct.
    Returns True if the guess is correct and False otherwise.
    """
    return correct_answer == guess


if __name__ == '__main__':

    win = False
    points = 3
    answer = random_number()
    while not win and points > 0:
        input_guess = one_guess()
        win = check_guess(answer, input_guess)
        if not win:
            print('Wrong, try again!')
            points -= 1

    if points > 0:
        print('Congratulations! You won {} points.'.format(points))
    else:
        print('You lost. Correct answer: {}.'.format(answer))
