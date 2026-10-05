from random import randint
friend="ram"

randomValue=randint(1,2)

user=...
match(randomValue):
    case 1: user="ram"
    case 2: user="shyam"
    case _: user=...
    
    
if user==friend:
    print("user is friend")
else:
    print("user is not friend")
