a=input("Enter string: ")
b=a.split(",")
c=len(b)-1
for i in range(len(b)):
 for j in range(len(b)):
  if(b[i]>b[j]):
   temp=b[i]
   b[i]=b[j]
   b[j]=temp
print("max: ",b[0])
print("min: ",b[c])
