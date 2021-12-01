#Pant style pattern of numbers
# 5 4 3 2 1 1 2 3 4 5 

# 5 4 3 2     2 3 4 5 

# 5 4 3         3 4 5 

# 5 4             4 5 

# 5                 5
n = int(input("Enter the Number: "))
for i in range(1,n+1):
    for j in range(n,i-1,-1,):
        print(j,end=" ")
    for j in range(2,i+1):
        print(" ",end=" ")
    for j in range(2,i+1):
        print(" ",end=" ")
    for j in range(i,n+1):
        print(j,end=" ")
    print()
