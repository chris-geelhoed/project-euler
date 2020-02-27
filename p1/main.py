'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

from functools import reduce
result = reduce(lambda t, i: (t + i) if i % 3 is 0 or i % 5 is 0 else t, range(1000), 0)
print(result)