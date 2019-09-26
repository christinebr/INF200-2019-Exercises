from src.christine_brinchmann_ex.ex01.letter_counts import letter_freq


def char_counts(textfilename):
    """

    Parameters
    ----------
    textfilename: the filename of the file which is opened using utf-8
    encoding. The function then reads the entire file into one string.

    Returns
    -------
    A list with the occurrences of character codes, between 0 and 255, in the
    file opened. char_code_counts[i] gives the occurrences of character code i.

    """

    infile = open(textfilename, 'r', encoding='utf-8')
    single_string = infile.read()
    infile.close()

    freq_char = letter_freq(single_string)

    char_code_counts = [0]*256
    for letter, count in freq_char.items():
        index = ord(letter)
        char_code_counts[index] = count

    return char_code_counts


if __name__ == '__main__':

    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )
