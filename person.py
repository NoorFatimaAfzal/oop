from datetime import date

class person:
    def __init__(self,name,country,date_of_birth):
        self.name=name
        self.country=country
        self.date_of_birth=date_of_birth
    def calculate_age(self):
        today=date.today()
        age=today.year - self.date_of_birth.year
        return age

name=input("Enter name of 1st person: ")
country=input("Enter name of country of 1st person: ")
date_of_birth = input("Enter date_of_birth YYYY,MM,DD: ")
year,month,day=map(int,date_of_birth.split(","))
date_of_birth=date(year,month,day)
person1=person(name,country,date_of_birth)
print(person1.calculate_age())

