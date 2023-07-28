import webbrowser
print(webbrowser)
a=str(input("choose your place :"))
def kerala():
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=SV1yzsSzUww&t=11s")

def tamilnadu():
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=l0FbXglafqU")


if(a=="tamilnadu"):
    tamilnadu()
elif(a=="kerala"):
     kerala()

    


