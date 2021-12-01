#Another inverted half pyramid pattern with number
# 0 1 2 3 4 5 
# 0 1 2 3 4 
# 0 1 2 3 
# 0 1 2 
# 0 1
n = int(input("Enter the Number: "))
for i in range(n):
    for j in range(0,n+1-i):
        print(j,end=" ")
    print()