#Equilateral triangle pattern of characters/alphabets
    #         A  
    #        B C  
    #       D E F  
    #      G H I J  
    #     K L M N O  
    #    P Q R S T U  
    #   V W X Y Z [ \  

n = int(input("Enter the Number: "))
a=65
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(" ",end="")
    for k in range(1,i+1):
        character = chr(a)
        print(character,end=" ")
        a+=1
    print()