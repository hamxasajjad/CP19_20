a=input("Enter paragraph: ")
b=a.split(".")
e=len(b)-1
for i in range(0,e):
 if(i==0):
  c=b[i]
  d=c[0].upper()
  print(d+c[1:])
 else:
  c=b[i]
  d=c[1].upper()
  print(d+c[2:])