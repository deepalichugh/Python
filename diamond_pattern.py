def diamond_pattern(n):
  for i in range(n//2+1):
    for k in range(n//2-i, 0, -1):
      print(" ", end = '')
    for j in range(2*i+1):
      print("*", end = '')
    print()
  for i in range(n//2):
    for j in range(i+1):
      print(" ", end = '')
    for l in range(2*(n//2-i), 1, -1):
      print("*", end = '')
    print()

n = int(input())
diamond_pattern(n)