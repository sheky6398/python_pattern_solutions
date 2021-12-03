# C Pattern 
#   * * * * * 
# *           
# *           
# *           
# *           
#   * * * * * 
n = int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 and j!=1 or i==n and j!=1 or j==1 and i not in [1,n]:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
