"""Problem-1: Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
  Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
  Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string"""
 
class Caluclator:
    def __init__(self,a:float,b:float):
        self.a=a
        self.b=b
    def caluclate_operations(self,operation_name:str):
        if operation_name=="add":
            return self.a+self.b
        elif operation_name=='sub':
            return self.a-self.b
        elif operation_name=='multi':
            return self.a*self.b
        elif operation_name=='divi':
            if self.a!=0:
                return self.a/self.b
            else:
                return "Zero is not valid"
        else:
            return "invalid"
c=Caluclator(10,2)
print(c.caluclate_operations("add"))
print(c.caluclate_operations("sub"))
print(c.caluclate_operations("multi"))
print(c.caluclate_operations("divi"))
