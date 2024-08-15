from datetime import datetime

class Person:
    def __init__(self,name,country,dob):
        self.name = name
        self.country = country
        self.dob = dob
    
    def person_age_display(self):
        print("Name of person is: ",self.name)
        print("The person is from: ",self.country)
        print("The person is ",int(datetime.now().year)-int(self.dob[-4:]),"years old")

P1 = Person("Bleh","UngaBungaLand","00-00-1900")
P1.person_age_display()