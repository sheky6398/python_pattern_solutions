#Right triangle pyramid of Stars
#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 
n = int(input("Enter the Number: "))
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print()