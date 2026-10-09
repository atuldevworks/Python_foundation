from csv import writer,DictWriter,DictReader

movies=[
    {"name":"joy of panda","date":"2026-08-29"},
    {"name":"joy of tiger","date":"2026-08-20"},
    {"name":"joy of lion","date":"2026-08-09"},
    {"name":"joy of panther","date":"2026-08-19"}  
    
    
]
path='Section06/sf004.csv'

file=open(path,'w')
writer=DictWriter(f=file,fieldnames=['name','date'])
writer.writeheader()
writer.writerows(movies)


file.close()


file=open(path,'r')

reader=DictReader(file,fieldnames=['name','date'])
for i in reader:
    print(i["name"])