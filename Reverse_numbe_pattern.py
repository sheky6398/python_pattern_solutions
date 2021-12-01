#Reverse number pattern
# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3 
# 2 2 
# 1
n = int(input("Enter the Number: "))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(i,end=" ")
    print()