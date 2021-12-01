#Inverted Pyramid pattern with the same digit
# 5 5 5 5 5 
# 5 5 5 5 
# 5 5 5 
# 5 5 
# 5
n = int(input("Enter the Number: "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(n,end=" ")
    print()