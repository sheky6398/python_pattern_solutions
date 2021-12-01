#Right down mirror star Pattern
# *****
#  ****
#   ***
#    **
#     *
n = int(input("Enter the Number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(" ",end=" ")
    for k in range(i,n+1):
        print("*",end=" ")
    print()