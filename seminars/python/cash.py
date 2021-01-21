"""
Cash.
Write a program that asks the user to type in an amount of money
and prints the minimum number of U.S. coins required to make change.
Assume you can use quarters(25¢), dimes(10¢), nickels(5¢), and pennies (1¢).

Hint: to choose which coin to use next, use the largest coin possible.
"""

import string

class PluralFormatter(string.Formatter):
  def format_field(self, value, format_spec):
    if format_spec.startswith('plural,'):
      words = format_spec.split(',')
      if value == 1:
          return words[1]
      else:
          return words[2]
    else:
      return super().format_field(value, format_spec)


def main():
  while True:
    amount = float(input("Enter amount in $: "))
    if amount > 0:
      break

  cents = round(amount * 100)
  get_change(cents)


def get_change(cents):
  q, d, n, p = (0,)*4
  print("Here is your change: ")

  while cents >= 25:
    q += 1
    cents -= 25
  while cents >= 10:
    d += 1
    cents -= 10
  while cents >= 5:
    n += 1
    cents -= 5
  while cents >= 1:
    p += 1
    cents -= 1

  fmt = PluralFormatter()
  print(fmt.format('{0} quarter{0:plural,,s}, {1} dime{1:plural,,s}, {2} nickel{2:plural,,s}, and {3} {3:plural,penny,pennies}.', q, d, n, p))


main()