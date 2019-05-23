a=input("Enter first sentence: ")
b=input("Enter second sentence: ")

a=a.split()
b=b.split()

for i in range(0,len(a)):
 for j in range(0,len(b)):
  if(a[i]==b[j]):
   print(a[i])