tamil=int(input("enter the mark:"))
english=int(input("enter the mark:"))
maths=int(input("enter the mark:"))
print("tamil :",tamil)
print("english :",english)
print("maths :",maths)
tot=tamil+english+maths
print("total :",tot)
avg=tot/3
print("average :",avg)

if tamil>40 and english>40 and maths>40:
    print("result = pass")
else:
    print("result = fail")

if avg>=80:
    print("grade=A+")
    if avg<=79 and avg>=60:
        print("grade=b")




        if avg>=40 and avg<=59:
            print("grade=c")
else:
    print("grade=D")






