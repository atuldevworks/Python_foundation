from functools import reduce
list1=[i for i in range(90)]
data=filter(lambda x:x%3==1,list1)
print(list(data))

lst2=list(map(lambda x:x*3,list1))
print(lst2)


lst3=reduce(lambda x:x/2,list1)