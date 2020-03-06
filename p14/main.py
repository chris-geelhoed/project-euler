'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''
map = {}

def collatz(n):
  chain = [n]
  while (True):
    head = chain[-1]
    steps = len(chain)
    if head == 1:
      break
    elif head in map:
      steps += map[head] - 1
      break
    else:
      chain.append(int(head / 2 if head % 2 == 0 else 3 * head + 1))
  for index, val in enumerate(chain):
    map[val] = steps - index
  return steps

largest = {
  'number': 0,
  'value': 0
}
for i in range(1, 10**6):
  c = collatz(i)
  if c > largest['value']:
    largest = {
      'number': i,
      'value': c
    }

print(largest)
