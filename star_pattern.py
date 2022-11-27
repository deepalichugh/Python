# For N = 5, print
#     *
#    ***
#   *****
#  *******
# *********

def star_pattern(n):
  for i in range(n, 0, -1):
    for j in range(i-1):
      print(" ", end = '')
    for k in range(1, 2*(n-i)+2):
      print("*", end = '')
    print()

n = int(input())
star_pattern(n)