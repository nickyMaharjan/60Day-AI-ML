l = 1
for i in range(5,0,-1):
    j=1
    while j <=9:
        if j == i:
            for k in range(1, l+1):
                print("*", end="")
                j+=1
        else:
            print(" ",end="")
            j+=1
    print()
    l+=2

l = 9
for i in range(5):
    j = 1
    while j<=9:
        if j == i+1:
            for k in range(1,l+1):
                print("*",end = "")
                j+=1
        else:
            print(" ", end = "")
            j+=1
    print()
    l-=2

