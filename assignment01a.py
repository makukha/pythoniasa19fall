"""
Assignment 1-A
==============

Write fuction that generates the text below; use at least variables and f-strings.
For those who are already familiar with Python – write the best code you can to conform to the Zen of Python.

>>> from pathlib import Path
>>> poem() == Path('data/poem-en.txt').read_text()
True
"""

def poem():

    chain = (
        'farmer sowing his corn', 'kept',
        'cock that crowed in the morn', 'waked',
        'priest all shaven and shorn', 'married',
        'man all tattered and torn', 'kissed',
        'maiden all forlorn', 'milked',
        'cow with the crumpled horn', 'tossed',
        'dog', 'worried',
        'cat', 'killed',
        'rat', 'ate',
        'malt', 'lay in',
        'house that Jack built',
        )

    def verse(chain):
        comma = lambda i: ',' if (i < (len(chain) // 2 - 1)) else ''
        text = f'This is the {chain[0]}'
        text += ''.join(f'{comma(i)}\nThat {p} the {o}' for i, (p, o) in enumerate(zip(chain[1::2], chain[2::2])))
        return text + '.\n'

    return '\n'.join(verse(chain[i-1:]) for i in range(len(chain), 0, -2))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
