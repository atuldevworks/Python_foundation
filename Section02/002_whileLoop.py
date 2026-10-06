isLearing=True
count=0
while isLearing==True:
    print(count)
    count+=1
    print("User is learing {}".format(count))
    isLearing=bool(input("enter any single character to continue  to discontinue or True to continue\n"))
    if isLearing!=True:
        break
    