'''
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''
from functools import lru_cache

@lru_cache(maxsize=None)
def tri(n):
  return 1 if n is 1 else n + tri(n - 1)

def divisors(n):
  x = 2
  divs = set()
  divs.add(1)
  while n > 1:
    if n % x == 0:
      n = n / x
      divs.update([div * x for div in divs])
    else:
      x += 1
  return divs

limit = 500
n = 1
d = set()
while len(d) < limit:
  t = tri(n)
  d = divisors(t)
  n += 1

print(t)













