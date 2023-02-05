def diamond_pattern(n):
    for i in range(n//2+1):
        for j in range(n//2-i, 0, -1):
            print(" ", end="")
        for k in range(i+1):
            print("*", end="")
        for l in range(i):
            print("*",end="")
        print("")
    for i in range(n//2):
        for j in range(i+1):
            print(" ", end="")
        for k in range(n//2-i, 0, -1):
            print("*", end="")
        for l in range(n//2-i-1):
            print("*",end="")
        print("")

diamond_pattern(3)