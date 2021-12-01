#Double the number pattern
#    1 
#    2    1 
#    4    2    1 
#    8    4    2    1 
#   16    8    4    2    1 
#   32   16    8    4    2    1 
#   64   32   16    8    4    2    1 
#  128   64   32   16    8    4    2    1
n=int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(-1+i,-1,-1):
        print(2**j,end=" ")
    print()
