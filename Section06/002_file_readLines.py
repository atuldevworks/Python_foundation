

path='Section06/sf002.txt'

file=open(path,'r')
lines=file.readlines()
items={f.strip().upper() for f in lines}
print(items)
file.close()
