#Another diamond pattern of star
#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *
n = int(input("Enter Odd Value: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j==n//2+2 or   i-j==n//2 or j-i==n//2 or i+j==n+n//2+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()