#Right start pattern of star
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 
n = int(input("Enter the Number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print("*",end=" ")
    print()