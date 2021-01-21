def main():
  # multiple 2 times table from range 0 to 9
  for i in range(10):
    multiply(2,i)

# multiply 2 numbers
def multiply(x,y):
  product = x * y
  print(x, "*", y, "=", product)

main()