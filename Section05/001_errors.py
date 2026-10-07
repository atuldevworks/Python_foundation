'''
Index error
Key Error
Name Error
Attribute Error
RuntimeError
SyntaxError
TabError
ValueError

'''
class CustomError(Exception):
    
    def __init__(self,message,code):
        msg="this is error message:- {} : {}".format(message,code)
        super().__init__(msg)
        
        


class Drive:
    def __init__(self,d):
        self.d=d
        
        
    def func1(self):
        raise CustomError("hello Errror",300)
    
    


d1=Drive(12)


try:
    d1.func1()
except CustomError as e:
    print(e)
    
else:
    print("else")
    
finally:
    print("done")


        
        
        
    