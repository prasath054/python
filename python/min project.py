print("******___JOURNEYS OF WONDAR___******")
print("LOGIN :")
name=str(input("enter your name :"))
place=str(input("enter your place :"))
ph=int(input("enter your phone no :"))
email=str(input("enter the email-id :"))


print("*****TOURIST PLACE*****")
import webbrowser

print("tamilnadu")
print("kerala")
print("karnataka")
a=int(input("choose your place :"))

def kerala():
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=SV1yzsSzUww&t=11s")

def tamilnadu():
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=l0FbXglafqU")

def karnataka():
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=WuMClj9czjg")

if(a==1):
    tamilnadu()
elif(a==2):
    kerala()
elif(a==3):
    karnataka()

print("ENTER YOUR DETAILES :")



print("family")
print("student")
a=int(input("choose trip :"))


fname=[]
fage=[]
cname=[]
cage=[]
z={}
def family():
    totalfamily=int(input("enter total members :"))
    adult=int(input("enter adult members :"))
    
    for i in range(0,adult):
        i=str(input("enter name :"))
        fname.append(i)
        
        
        j=int(input("enter age :"))
        fage.append(j)
        b=("enter name :",i)
        c=("enter age :",j)
        
    child=int(input("enter child members :"))
    for k in range(0,child):
        k=str(input("enter name :"))
        
        cname.append(k)
        l=int(input("enter age :"))
        
        cage.append(l)
        d=("enter name :",k)
        e=("enter age :",l)



def student():
    collegename=str(input("enter your college name :"))
    department=str(input("enter your department :"))
    totalstudent=int(input("total student :"))

if(a==1):
    family()
elif(a==2):
    student()

def familydetailes():
    print("******___JOURNEYS OF WONDAR___******")
    print("Name :",name)
    print("Trip start place :",place)
    print("phone number :",ph)
    print("E-mail ID :",email)
    print("*****family members***** ")

    z={}
    for key in fname:
        for value in fage:
            z[key] = value
            fage.remove(value)
            for i, j in z.items():
                print("name :",i)
                print("age :",j)

    y={}
    for key in cname:
        for value in cage:
            y[key] = value
            cage.remove(value)
            for k,l in y.items():
                print("child name :",k)
                print("child age :",l)


    
    
def collegestudent():
    print("*****___JOURNEYS OF WONDAR___*****")
    print("Name :",name)
    print("Trip start place :",place)
    print("phone number :",ph)
    print("E-mail ID :",email)
    print("college name :",collegename)
    print("Departmrnt :",department)
    print("Total student :",totalstudent)


print("family")
print("student")
x=int(input("enter number :"))
if x==1:
    familydetailes()
elif x==2:
    collegestudent()









        


    



