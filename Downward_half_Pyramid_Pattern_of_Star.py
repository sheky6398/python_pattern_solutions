#Downward half-Pyramid Pattern of Star
# * * * * *  
# * * * *  
# * * *  
# * *  
# *
n = int(input("Enter the Number: "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print("*",end=" ")
    print()