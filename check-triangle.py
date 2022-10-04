side1 = int(input("Enter first side"));
side2 = int(input("Enter second side"));
side3 = int(input("Enter third side"));
if side1 == side2 and side1 == side3:
  print(1) #Equilateral
elif ((side1 == side2 and side1 != side3) or (side1 == side3 and side1 != side2) or (side2 == side3 and side2 != side1)):
  print(0)  #Isosceles
else:
  print(-1) #Scalene
