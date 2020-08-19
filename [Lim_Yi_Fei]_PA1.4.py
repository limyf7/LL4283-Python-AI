'''
14.5 + 5.5

Simple and clean code. However, some confusion between the use of the return and print statements.
'''

dictionary = {'see': 'saw', 'bear': 'bore', 'sell': 'sold', 'forget': 'forgot', 'go': 'went', 'hurt': 'hurt',
              'ride': 'rode', 'leave': 'left', 'take': 'took', 'be': 'was'}


def Present2Past(verb):
    try:
        return print(dictionary[verb])

    except KeyError:
        return print('')

Present2Past('see')

# Typing Present2Past('word') will give you the past tense of the word.
# If the word is not found in dictionary, an empty string will be returned.

'''
def Present2Past(verb):
    output = 'The past tense of "{}" is '.format(verb)

    try:
        return print(output + '"{}"'.format(dictionary[verb]))

    except KeyError:
        return print('')

'''