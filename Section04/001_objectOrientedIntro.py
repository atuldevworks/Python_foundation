class Student:
    #magic method
    def __init__(self,newName,newGrades):
        self.name=newName
        self.grades=newGrades
        
        
    def average(self):
        return sum(self.grades)/len(self.grades)
    
    def __len__(self):
        return len(globals())
    
    #magic Method
    def __del__(self):
        print("object deleted")
        
    def __getitem__(self, i):
        lst1=list(globals().values())
        return lst1[i]
    def __repr__(self):
        return f'Studnet with {len(self)} objects'
    
std001=Student("atul",[1,2,3,2,4])


print(std001.average())
#parameter naming
print(Student('Atul',[1,3,4,4,2]).average())


#magic methods
print(len(std001))


print(std001[3])
print("*****")
for i in std001:
    print(i)