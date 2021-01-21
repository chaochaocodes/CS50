"""
Grid.
Write a program that asks the user to type in a number n
and then prints an n x n grid of hash marks.
For example, a 3x3 grid would look like:

 ###
 ###
 ###

"""

n = int(input("n: "))  

# prints n hashmarks in a row
for i in range(n):
  # print n rows
  for j in range(n):
    print("#", end="")
  # print empty for new line after each row
  print()