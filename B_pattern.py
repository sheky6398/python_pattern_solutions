#B_pattern.py
# * * *   
# *     * 
# * * *   
# *     * 
# * * *  
for i in range(1,6):
    for j in range(1,5):
        if j==1 or i in [1,3,5] and j!=4 or i==2 and j==4 or i==4 and j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()