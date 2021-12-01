# A character Pattern
#   ***                                                                                                         
#  *   *                                                                                                        
#  *   *                                                                                                        
#  *****                                                                                                        
#  *   *                                                                                                        
#  *   *                                                                                                        
#  *   * 
n=int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 and j!=1 and j!=n or j==1 and i!=1 or j==n and i!=1 or i==n//2+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
