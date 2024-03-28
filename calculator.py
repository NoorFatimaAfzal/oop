class calculator:
    def __init__(self):
        print("This is class of simple \n arithmatic calculator!")
    def add(self,x,y):
        return x+y
    def subtract(self,x,y):
        return x-y
    def square(self,x):
        return x**2
    def divide(self,x,y):
        try:
            ans=x/y
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            try:
                y=int(input("Enter y agian"))
            except ValueError:
                print("Error: Input must be a number.")
                y=int(input("Enter y agian"))
                return x/y
            return x/y
        return ans
                
calculator1=calculator()
print(calculator1.divide(5,0))