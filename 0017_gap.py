"""
Gap in Primes


The prime numbers are not regularly spaced. For example from 2 to 3 the gap is 1. From 3 to 5 the gap is 2. From 7 to 11 it is 4. Between 2 and 50 we have the following pairs of 2-gaps primes: 3-5, 5-7, 11-13, 17-19, 29-31, 41-43

A prime gap of length n is a run of n-1 consecutive composite numbers between two successive primes (see: http://mathworld.wolfram.com/PrimeGaps.html).

We will write a function gap with parameters:

g (integer >= 2) which indicates the gap we are looking for

m (integer > 2) which gives the start of the search (m inclusive)

n (integer >= m) which gives the end of the search (n inclusive)

n won't go beyond 1100000.

In the example above gap(2, 3, 50) will return [3, 5] or (3, 5) or {3, 5} which is the first pair between 3 and 50 with
a 2-gap.

So this function should return the first pair of two prime numbers spaced with a gap of g between the limits m, n if
these numbers exist otherwise `nil or null or None or Nothing (or ... depending on the language).

In C++, Lua: return in such a case {0, 0}. In F#: return [||]. In Kotlin, Dart and Prolog: return []. In Pascal: return
Type TGap (0, 0).

Examples:
gap(2, 5, 7) --> [5, 7] or (5, 7) or {5, 7}

gap(2, 5, 5) --> nil. In C++ {0, 0}. In F# [||]. In Kotlin, Dart and Prolog return []`

gap(4, 130, 200) --> [163, 167] or (163, 167) or {163, 167}

([193, 197] is also such a 4-gap primes between 130 and 200 but it's not the first pair)

gap(6,100,110) --> nil or {0, 0} or ... : between 100 and 110 we have 101, 103, 107, 109 but 101-107is not a 6-gap
because there is 103in between and 103-109is not a 6-gap because there is 107in between.

You can see more examples of return in Sample Tests.

Note for Go
For Go: nil slice is expected when there are no gap between m and n. Example: gap(11,30000,100000) --> nil

Ref
https://en.wikipedia.org/wiki/Prime_gap
"""


def gap(g, m, n):
    # shows the input
    print(f'g: {g}\tm: {m}\tn: {n}\n')

    # verify if inputs are satisfied
    if g >= 2 and m > 2 and n >= m:
        primes = []
        founded = False

        # Fill a list with prime numbers in wich m <= prime number <= n
        for num in range(m, n + 1, 1):
            if is_prime(num):
                primes.append(num)
            # One way I founded to the code runs and finalize fast.
            # Fills till find the one
            if len(primes) > 1:
                if (primes[-1] - primes[-2]) == g:
                    founded = True
                    break
        # shows primes list filled until the moment that found the one
        print('-> Primes List:\n\t', primes, '\n', sep='')

        # if founded, returns the one e shows wich are
        if founded:
            print(f'-> Founded:\n\t[{primes[-2]}, {primes[-1]}]')
            return [primes[-2], primes[-1]]

    print('Returning "None"')
    return None


# code is_prime() from previus challenge
def is_prime(num):
    if num < 2:
        return False
    elif num == 2 or num == 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    else:
        for x in range(5, int(1 + num ** (1 / 2)), 6):
            # 6n + 1 or 6n - 1, with n = natural > 1
            if num % x == 0 or num % (x + 2) == 0:
                return False
    return True
