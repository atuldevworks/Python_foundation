
path='Section06/sf003.csv'
file=open(path,'r')
lines=[f.strip() for f in file.readlines() ]
file.close()

data=lines[1:]

final_list=[]
x=0
for i in data:
   
    record=i.split(',')
    label=["name","roll","address"]
    details=dict(zip(label,record))
    final_list.append(details)
    
    


print()
for i in final_list:
    print("name : ",i["name"],"\t", "roll : ",i["roll"],"\t","address : ",i["address"])
    print()



        
    
    