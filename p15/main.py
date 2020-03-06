'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
'''
n = 20
map = {}

def f(x, y):
  if x > n or y > n:
    return 0
  if x == n or y == n:
    return 1
  key = str(x) + str(y)
  if key in map:
    return map[key]
  ways = f(x + 1, y) + f(x, y + 1)
  map[key] = ways
  map[key[::-1]] = ways # f(x, y) = f(y, x)
  return ways

ways = f(0, 0)
print(ways)