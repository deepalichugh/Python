# For N = 5, print
#     1
#    232
#   34543
#  4567654
# 567898765

def triang_of_nums(n):
  counter = 0
  for i in range(1,n+1):
    counter = i
    for j in range(n-i):
      print(" ", end = '')
    for k in range(1,i+1):
      print(counter, end = '')
      counter = counter + 1
    for l in range(i-1):
      print(counter-2, end = '')
      counter = counter-1
    print()

n = int(input())
triang_of_nums(n)