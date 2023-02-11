def rectangular_numbers(n):
    for i in range(n):
        counter=n-i+1
        for j in range(i+1):
            print(n-j, end="")
        for k in range(n-i-1):
            print(n-i, end="")
        for l in range(n-i-1):
            print(n-i, end="")
        for m in range(1, i+1):
            print(counter, end="")
            counter=counter+1
        print("\n")
    for i in range(n-1):
        counter = n
        for j in range(n-i-1,0,-1):
            print(counter, end="")
            counter=counter-1
        for k in range(i+1):
            print(i+2,end="")
        print("\n")



rectangular_numbers(4)
    