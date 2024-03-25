class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_average(self):
        sum=0
        for values in self.marks:
            sum+=values
        print(f"hi, {self.name} your average marks are {sum/len(self.marks)}")
        return sum/len(self.marks)

    def congratulate(self):
        average = self.get_average()
        if average > 90:
            print(f"Congratulations {self.name}!")
        else:
            print(f"Work hard {self.name}!")

s1=student("noor",[99,99,99])
s1.get_average()
s1.congratulate()

s2=student("fatima",[100,100,100])
s2.get_average()
s2.congratulate()
