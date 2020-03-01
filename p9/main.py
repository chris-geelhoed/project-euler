'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
# a + b + c = 1000
# c = 1000 - a - b
# a^2 + b^2 = (1000 - a - b)(1000 - a - b)
# a^2 + b^2 = 1000^2 - 1000a - 1000b - 1000a + a^2 + ab -1000b + ab + b^2
# 0 = 1000^2 - 1000a - 1000b - 1000a + ab -1000b + ab
# 0 = 1000^2 - 2000a - 2000b + 2ab
# -1000^2 + 2000a = b(-2000 + 2a)
# (-1000^2 + 2000a) / (-2000 + 2a) = b

for a in range(1, 10001):
  b = (-1000**2 + 2000 * a) / (-2000 + 2 * a)
  c = 1000 - a - b
  if b % 1 == 0 and b > 0 and c > 0:
    print(a, b, c)
    print(a*b*c)
    break




