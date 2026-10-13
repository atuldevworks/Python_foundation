def get_hundered():
    i=0
    
    while i<100:
        yield i
        i+=1
        


g=get_hundered()

print(next(g))
print(next(g))


class Hun:
    
    def __init__(self,m):
        self.num=0
        self.m=m
        
    def __next__(self):
        if self.num<self.m:
            curr=self.num
            self.num+=1
            return curr
        else:
            raise StopIteration()
        
    def __repr__(self):
        return self.num
    
    def __iter__(self):
        return self
   
    
print("*")    
    
a=Hun(10)

print(a.num)
a.__next__()
print(a.num)

print(next(a))
print(next(a))
print(next(a))
print(next(a)) 


for i in a:
    print(i," : ")
    

          
        

