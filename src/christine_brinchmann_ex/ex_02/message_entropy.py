# -*- coding: utf-8 -*-

__author__ = "Christine Brinchmann"
__email__ = "christibr@nmbu.no"

from math import log2

from src.christine_brinchmann_ex.ex01.letter_counts import letter_freq


def entropy(message):
    """

    Parameters
    ----------
    message: the message for which the entropy should be calculated

    Returns
    -------
    The entropy for the message calculated according to the equation
    H = - sum(p[i]*log2(p[i])), where p[i] is the frequency of one letter in
    the message.

    """
    freq = letter_freq(message)
    length_message = len(message)
    h = []
    for letter in freq:
        p = freq[letter] / length_message
        h.append(-p*log2(p))

    entropy_sum = sum(h)
    return entropy_sum


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
