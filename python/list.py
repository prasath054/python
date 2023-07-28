
a = ["Rash", "Kil", "Varsha"]
b = [1, 4, 5]

res = {}
for key in a:
    for value in b:
        res[key] = value
        b.remove(value)
        break


print( res)



a = {   'Ritika': 5,
        'Sam': 7, 
        'John': 10, 
        'Aadi': 8}
