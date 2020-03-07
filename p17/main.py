'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''
map = {
  0: '',
  1: 'one',
  2: 'two',
  3: 'three',
  4: 'four',
  5: 'five',
  6: 'six',
  7: 'seven',
  8: 'eight',
  9: 'nine',
  10: 'ten',
  11: 'eleven',
  12: 'twelve',
  13: 'thirteen',
  14: 'fourteen',
  15: 'fifteen',
  16: 'sixteen',
  17: 'seventeen',
  18: 'eighteen',
  19: 'nineteen',
  20: 'twenty',
  30: 'thirty',
  40: 'forty',
  50: 'fifty',
  60: 'sixty',
  70: 'seventy',
  80: 'eighty',
  90: 'ninety'
}

def write_num(n):
  m = ''
  if n == 1000:
    return 'onethousand'
  hundreds, tens, ones = [int(i) for i in str(n).zfill(3)]
  last_two_digits = 10 * tens + ones
  if hundreds > 0:
    m += map[hundreds] + 'hundred'
    if last_two_digits > 0:
      m += 'and'
  if last_two_digits < 20:
    return m + map[last_two_digits]
  return m + map[10 * tens] + map[ones]

print(sum(len(write_num(i)) for i in range(1, 1000 + 1)))

