import datetime
date = datetime.datetime.now() 
y=date.year
m=date.month
d=date.day
a=input("Enter Date: ")
b=a.split("/")
if(int(b[2])==y):
 if(int(b[1])==m):
  if(int(b[0])==d):
   print("Date is equal")
  elif(int(b[0])>d):
   print("Date is greater")
  else:
   print("Date is less")
 elif(int(b[1])>m):
  print("Date is greater")
 else:
  print("Date is less")
elif(int(b[2])>y):
 print("Date is greater")
else:
 print("Date is less")
