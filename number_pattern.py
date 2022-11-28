# For N = 5, print
# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321

def num_pattern(n):
  for i in range(1, n+1):
    for j in range(1, i+1):
      print(j, end='')
    for l in range(2*(n-i), 0, -1):
      print(" ", end='')
    for m in range(i, 0, -1):
      print(m, end='')
    print()


n = int(input())
num_pattern(n)