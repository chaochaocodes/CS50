""" 
Mario Pyramid. 
Write a program that asks the user to type in a number n
and then prints a pyramid of hash marks of height n.
For example, a pyramid of height 5 would look like:

    #
   ##
  ###
 ####
#####

"""
def main():
  # take user input
  while True:
    n = int(input("Enter a positive integer: "))
    if n > 0: 
      break

  mario_pyramid(n)

def mario_pyramid(n):
  # print n hash marks in a row
  for i in range(n):
    # print hash mark i times
    hash = (i+1) * '#'
    print(hash.rjust(n, ' '))

main()