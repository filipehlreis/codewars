"""
Valid Braces


Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return
true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}.
Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.

Examples
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False
"""


def validBraces(string):
    print(string)

    # define lists and dictionary to verify the string input. If you wanna add more symbols to define types of
    # beginning and ending, it is necessary to fill
    # the "braces_open", "braces_close" and "braces_dict".
    braces_open = ['(', '{', '[']
    braces_close = [')', '}', ']']
    braces_dict = {
        '(': 1,
        ')': 2,
        '{': 3,
        '}': 4,
        '[': 5,
        ']': 6
    }
    braces_input = []
    braces_expected = []

    # first verification of errors.
    if string[0] in braces_close or string[-1] in braces_open:
        return False

    # runs each index of string
    for k in range(len(string)):
        # if actual index is some symbol that opens:
        if string[k] in braces_open:
            # add the actual and the expected to be closed later.
            braces_input.append(braces_dict.get(string[k]))
            braces_expected.append(braces_dict.get(string[k]) + 1)
        else:
            # is the actual index is a symbol expected to close, pops the list "braces_input" and "braces_expected" in
            # order to empty.
            if len(braces_expected):
                if braces_dict.get(string[k]) == braces_expected[-1]:
                    braces_input.pop()
                    braces_expected.pop()

    # if "braces_input" and "braces_expected" are empty, so the verification is completed and the input was OK, True,
    # else is not OK, False, failed in some moment.
    return True if braces_input == [] and braces_expected == [] else False


"""
Some solutions founded in CodeWars that it's interesting.

"""


def validBraces1(s):
    while '{}' in s or '()' in s or '[]' in s:
        s = s.replace('{}', '')
        s = s.replace('[]', '')
        s = s.replace('()', '')
    return s == ''
