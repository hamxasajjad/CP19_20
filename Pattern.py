
     #PATTERN 1

num=int(input("Enter length of a Pattern ="))
def pattern():
        for i in range (1,num+1):
            for k in range (1,(num+1)-i):
                print(" ",end=" ")    
            for j in range (1,1*i):
                print("8","4",end=" ")    
            print("8")  
pattern()      