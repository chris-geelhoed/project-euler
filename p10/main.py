'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
from math import ceil

limit = 2*10**6
box = {}
for i in range(2, limit):
  box[i] = True

for j in range(2, ceil(limit ** 0.5) + 1):
  if not box[j]:
    continue
  m = 2
  while m * j < limit:
    box[m * j] = False
    m += 1
s = sum([key for key, val in box.items() if val])
print(s)










