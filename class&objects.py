class student:

    name="Noor"
    color="blue" #class attr
    def __init__(self,name):
        self.name=name
        self.color="white" #obj attr
        print("ye constructor hai...har dafa hona hai.")

s1=student("noorfatima")
print(s1.name,s1.color) #print object wala hoga
s2=student("fatima")
print(s2.name,s2.color)