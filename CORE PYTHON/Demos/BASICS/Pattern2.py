for i in range(5,0,-1):
    for j in range(5,0,-1):
        if(i==1):
            print(j, end="")
        elif(i==1 or j==1 or j==4):
            print(j, end="")
        elif(i==3 or j==1 or j==3):
            print(j, end="")
        elif(i==4 or j==1 or j==2):
            print(j, end="")
        elif(i==5 or j==1):
            print(j, end="")
        else:
            print(" ", end="")
    print()

#hollow pattern 
for i in range(1,6):
    for j in range(1,6):
        if(i==1 or j==5 or i==5 or j==1):
            print(i ,end="")
    print()
