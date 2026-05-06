for i in range(1,6):
    for j in range(1,6):
        if(i==1 or i==3 or i==5):
            print("*",end="")
        elif(i==2 or i==4):
            print("$",end="")
        else:
            print(" ",end="")
    print()

for i in range(1,6):
    for j in range(1,6-i):
        print("*",end="")
    print()

for i in range(1,6):
    for j in range(1,i):
        print("*",end="")
    print() 

for i in range(1,6):
    for j in range(6-i,0,-1):
        print("*",end="")
    print()