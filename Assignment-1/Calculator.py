class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        print("Result of addition is: ",self.num1+self.num2)
    
    def subtract(self):
        print("Result of subraction is: ",self.num1-self.num2)

    def multiply(self):
        print("Result of multiplication is",self.num1*self.num2)

    def divide(self):
        print("Result of division is: ",self.num1/self.num2)

a = Calculator(6,3)    
a.add()
a.subtract()
a.multiply()
a.divide()

        

