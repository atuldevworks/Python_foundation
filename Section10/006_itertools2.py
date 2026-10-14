from itertools import combinations,permutations


str='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'

path='Comb001.txt'
file=open(path,'a+')
p1=permutations(str,r=11)
for i in p1:
    
    tempStr=""
    for j in i:
        tempStr+=j
    file.write(tempStr+"\n")
    
file.close()
    

    
    
