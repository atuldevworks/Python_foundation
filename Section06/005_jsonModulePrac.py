from json import load,dump

path='Section06/sf005.json'
path2='Section06/sf006.json'
file=open(path,'r')

data=load(file)
file.close()
print(data["friends"])
print(data["friends"][0]["age"])



data={
    "friends":[
        {
            "name":"atul",
            "age":23
        },
        {
            "name":"vimal",
            "age":29
        },
        {
            "name":"tiwari",
            "age":19
        }
    ],
    "enemy":[
        {
            "name":"enemy1",
            "age":34
        },
        {
                    "name":"enemy1",
                    "age":34
        },
        {
                            "name":"enemy2",
                            "age":39
                },
    ]
    
    
}

file=open(path2,'w')
dump(data,file)
file.close()