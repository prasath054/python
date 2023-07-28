a=open("C:\\Users\\Hi\\Documents\\ms1.txt","a+")
b=a.read()
#print(b)
'''c=len(b)
print(c)'''

for i in b:
    if i==" ":
        a.write("*")
        x=a.read()
        print(x)
    print(i)



