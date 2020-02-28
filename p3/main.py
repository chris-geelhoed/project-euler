'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
prime = 2
limit = 600851475143
while limit > 1:
  if limit % prime == 0:
    limit = limit / prime
  else:
    prime += 1

print(prime)