def func1():
    print("hello")
    
    
func1()

def func2(a:int|None,b:int|None)->None:
    """_summary_\n
    This function 

    Args:
        a (int | None): _description_
        b (int | None): _description_
    """
    print(a+b)
    
    
lambdaFunction1=lambda x,y,z:x/y+z

print(lambdaFunction1(13,44,34))


print((lambda x,y:x+y)(2,4))