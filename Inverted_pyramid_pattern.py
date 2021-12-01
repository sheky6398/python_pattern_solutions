#Inverted pyramid pattern
# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3 
# 4 4 
# 5
n = int(input("Enter the Number: "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(i,end=" ")
    print()