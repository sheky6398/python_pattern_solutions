#Pant style pattern of stars
# ****************
# *******__*******
# ******____******
# *****______*****
# ****________****
# ***__________***
# **____________**
# *______________*
n = int(input("Enter the Number: "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print("*",end="")
    for j in range(1,i):
        print("-",end="")
    for j in range(1,i):
        print("-",end="")
    for k in range(i,n+1):
        print("*",end="")
    print()