doubledNumbers=[n*2 for n in range(45) if n/3==3]
print(doubledNumbers)


friends=['ram','shyam','rohan']
guests=['mohan','rohan','atul','ram']

print(set([f.lower() for f in friends]).intersection(set([f.lower() for f in guests])))