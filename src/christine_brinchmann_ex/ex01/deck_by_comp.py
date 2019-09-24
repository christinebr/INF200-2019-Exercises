SUITS = ('C', 'S', 'H', 'D')
VALUES = range(1, 14)


def deck_loop():
    deck = []
    for suit in SUITS:
        for val in VALUES:
            deck.append((suit, val))
    return deck


def deck_comp():
    """ Returns a deck of cards as a list of 2-tuples.
    The deck of cards have four suits (clubs (C), spades (S), hearts (H) and
    diamonds (D)) and each suit have cards going from 1 to 13.
    Each tuple represents one card, the first element is the suit and the
    second element is the value of the card. 
    """
    return [(suit, val) for suit in SUITS for val in VALUES]


if __name__ == '__main__':
    if deck_loop() != deck_comp():
        print('ERROR!')
