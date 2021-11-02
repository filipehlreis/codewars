"""
Highest Scoring Word


Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
"""


def high(x):
    letters_score = (
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z'
    )
    words = tuple(''.join(x).split())
    words_soma = []
    for word in words:
        soma = 0
        for letters in word:
            soma += letters_score.index(letters) + 1
        words_soma.append(soma)
    return words[words_soma.index(max(words_soma))]
