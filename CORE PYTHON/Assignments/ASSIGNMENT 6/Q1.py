#program to print different patterns 
#a
for i in range(1,6):
    for j in range (1,6):
        if(i==1 or j==1 or i==5 or j==5):
            print("*",end="")
        else:
            print(" ",end="")
    print()

#b
num=1
for i in range(1,5):
    for j in range(i):
        print(num,end="")
        num+=1
    print()

#c
for i in range(1,7):
    for j in range(1,6):
        if (i==1 or j==1 or i==6 or j==5):
            print("*",end="")
        else:
            print(" ",end="")
    print()

#d
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(64+j),end="")
    print()

#e
for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end="")
    for k in range(1,i*2):
        print("*",end="")
    print()