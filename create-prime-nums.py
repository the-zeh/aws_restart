##########  by Zehra Saglam    Lab 141 Challenge

f = open("myfile.txt", "w")
f.write("2\n")

for i in range(3,250):
  isPrime = True
  if(i%2!=0):
    x=2
    while (x<i) and (isPrime==True):
      if(i%x==0):
        isPrime = False
      x=x+1

    if(isPrime == True):
       print(i)
       f.write(str(i)+"\n")
  else:
    isPrime= False

f.close()