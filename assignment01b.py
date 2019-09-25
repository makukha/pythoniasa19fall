"""
Assignment 1-B (optional)
=========================

This assignment is similar to 1-A except that the poem is in Russian now.

>>> from pathlib import Path
>>> poem() == Path('data/poem-ru.txt').read_text()
True
"""

def poem():

    lines = (
        ('Вот дом, который построил Джек', lambda case: 'В доме, который построил Джек'),
        ('А это пшеница', lambda case: 'Которая в тёмном чулане хранится'),
        ('А это весёлая птица-синица', lambda case: 'Которая часто ворует пшеницу'),
        ('Вот кот', lambda case: 'Который пугает и ловит синицу'),
        ('Вот пёс без хвоста', lambda case: 'Который за шиворот треплет кота'),
        ('А это корова безрогая', lambda case: {
            'nom': 'Лягнувшая старого пса без хвоста',
            'acc': 'Лягнувшую старого пса без хвоста'}[case]),
        ('А это старушка, седая и строгая', lambda case: 'Которая доит корову безрогую'),
        ('А это ленивый и толстый пастух', lambda case: 'Который бранится с коровницей строгою'),
        ('Вот два петуха', lambda case: 'Которые будят того пастуха'),
        )

    def verse(i):
        comma = lambda j: ',' if (j > 0) else ''
        text = f'{lines[i][0]}'
        if i > 0:
            text += f',\n' + lines[i][1]('nom')
        text += ''.join(f'{comma(j)}\n' + lines[j][1]('acc') for j in range(i - 1, -1, -1))
        return text + '.\n'

    return '\n'.join(verse(i) for i in range(len(lines)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
