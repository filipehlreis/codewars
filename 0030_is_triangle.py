"""
Is this a triangle?


Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built
with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).
"""


def is_triangle(a, b, c):
    if (abs(b - c) < a < (b + c)) and (abs(a - c) < b < (a + c)) and (abs(a - b) < c < (a + b)):
        return True
    return False
