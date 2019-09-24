

def letter_freq(txt):
    """ Returns a dictionary with each character in a string (in alphabetic
     order) as keys and how many times they appears in the string as values.
    """
    text_lowercase = txt.lower()  # makes all the letters lowercase
    freq = {}  # creates an empty dictionary
    sorted_text = sorted(text_lowercase)  # sorts the letters alphabetically

    for character in sorted_text:
        if character in freq:
            freq[character] += 1
        else:
            freq[character] = 1
    return freq


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))
