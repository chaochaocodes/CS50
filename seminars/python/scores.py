def main():
  score1 = int(input("Score: "))
  score2 = int(input("Score: "))
  score3 = int(input("Score: "))

  print_score(score1)
  print_score(score2)
  print_score(score3)

def print_score(n):
  for i in range(n):
    # print nothing at end instead of newline
    print("#" , end = "")  
  print()

main()