def check_prime(num):
  if num <= 0:
    return

  for i in range(2, num):
    if(num % i != 0):
      return "Prime"
    else:
      return "Not prime"


num = int(input())
print(check_prime(num))