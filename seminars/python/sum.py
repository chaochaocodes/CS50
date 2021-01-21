"""
Sum.
Write a program that asks the user to type in ten integers
as input and then prints their sum.
"""

# ask user for type in integer
# loop to ask 10 times
# sum the integers
sum = 0

for i in range(10):
  n = int(input("Enter number: "))
  sum += n

print("Sum is: ", sum)
