#Pyramid of numbers up to 10
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10
n=int(input("Enter the number: "))
a=0
for i in range(1,n+1):
    for j in range(1,i+1):
        a+=1
        print(a,end=" ")
    print()