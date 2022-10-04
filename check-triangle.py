s1 = int(input("Enter first side"));
s2 = int(input("Enter second side"));
s3 = int(input("Enter third side"));
if s1 == s2 and s1== s3:
  print(1)
elif ((s1 == s2 and s1 != s3) or (s2 == s3 and s2 != s1) or (s3 == s1 and s3 != s2)):
  print(0)
else:
  print(-1)
