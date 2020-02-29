'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
limit = 20

def primes(n):
  x = 2
  p = {}
  while n > 1:
    if n % x == 0:
      n = n / x
      p[x] = 1 if x not in p else p[x] + 1
    else:
      x += 1
  return p

map = {}
for i in range(2, limit + 1):
  factors = primes(i)
  for prime, m in factors.items():
    if prime not in map or m > map[prime]:
      map[prime] = m

result = 1
for prime, n in map.items():
  result = result * prime ** n

print(result)











