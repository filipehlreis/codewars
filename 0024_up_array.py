"""
+1 Array


Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

the array can't be empty
only non-negative, single digit integers are allowed
Return nil (or your language's equivalent) for invalid inputs.

Examples
For example the array [2, 3, 9] equals 239, adding one would return the array [2, 4, 0].

[4, 3, 2, 5] would return [4, 3, 2, 6]
"""


def up_array(arr):
    try:
        if arr == []:
            return None
        for x in arr:
            if x < 0 or x > 9:
                return None
        i = 0
        size = len(arr)

        while arr[-1 - i] < 10 and i < len(arr):
            arr[-1 - i] += 1
            if arr[-1 - i] > 9:
                if abs(-1 - i) == len(arr):
                    arr.insert(0, 1)
                    arr[-1 - i] = 0
                    break
                arr[-1 - i] = 0
                i += 1
            else:
                break
    except Exception as e:
        print(e)
    return arr
