class calculate():
    def __init__(self,  num1, num2):
        self.num1=num1
        self.num2=num2

    def add(self, num1, num2):
        return num1+num2
    def sub(self,  num1, num2):
        return  num1-num2
    def mult(self,  num1, num2):
        return num1*num2
    def div(self,  num1, num2):
        return num1/num2
mynumber=calculate(50, 10)
print(my_number.add(100,15))
print(my_number.sub(150,25))
print(my_number.mult(200,30))
print(my_number.div(250,345))