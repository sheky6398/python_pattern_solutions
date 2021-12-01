#Alternate numbers pattern
# 1 
# 3 3 
# 5 5 5 
# 7 7 7 7 
# 9 9 9 9 9
n = int(input("Enter the Number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        a=(2*i-1)
        print(a,end=" ")
    print()