# only accept positive integer input
# exit loop when true
# booleans are capitalized in python

while True:
  n = int(input("Positive integer: "))
  if n > 0: 
    break

print(n)