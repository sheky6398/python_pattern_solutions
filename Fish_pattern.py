#Fish Pattern 
#     *             
#    * *          
#   * * *       * 
#  * * * *    * * 
# * * * * * * * * 
#  * * * *    * * 
#   * * *       * 
#    * *          
#     *   
n=int(input("Enter the number: "))
for i in range(1,n):
    for j in range(1,n-i):
        print("",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    for j in range(1,n-i):
        print(" ",end="")
    for j in range(1,n-i):
        print(" ",end=" ")
    for j in range(n//2,i+1):
        print("*",end=" ")
    print()
for i in range(1,n):
    for j in range(1,i+1):
        print("",end=" ")
    for j in range(i+1,n):
        print("*",end=" ")
    for j in range(1,i+1):
        print(" ",end="")
    for j in range(1,i+1):
        print(" ",end=" ")
    for j in range(i+n//2,n):
        print("*",end=" ")
    print()