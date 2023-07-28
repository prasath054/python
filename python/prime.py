x=0
y=20
for i in range(x,y+1):
    if i>0:
         for j in range(2,i):
             if(i%j==0):
                 break
         else:
             print(i)

           
