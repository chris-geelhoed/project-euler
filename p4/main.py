'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
d = 3
p = 0
bounds = range(10**(d - 1), 10**d)
for i in bounds:
  for j in bounds:
    n = i * j
    s = str(n)
    if n > p and s == s[::-1]:
      p = n
print(p)







