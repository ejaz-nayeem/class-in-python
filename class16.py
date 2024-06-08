class Person:
    def __init__(self, person_name:str, year_of_birth:int, ht_inches:int=None):
        self.__name=person_name
        self.__height=ht_inches
        self.__date_of_birth=year_of_birth
        
    def get_name(self):
        return self.__name
    def get_summary(self):
        return f"{self.__name},{self.__date_of_birth},{self.__height if self.__height is not None else 'invalid'}"
    def set_name(self,new_name):
        self.__name=new_name
    def get_year_of_birth(self):
        return self.__date_of_birth
    
        
a_person=Person("ejaz", 1990)
#print(a_person.set_name("muhammad ejaz bin nayeem"))

#print(a_person.get_summary())
#print(a_person.height)
#print(a_person.date_of_birth)
#print(a_person.name)
#print(a_person.get_name())
person_list=[]
person_list.append(Person("A", 1991, 70))
person_list.append(Person("B", 1989))
person_list.append(Person("C", 1993))
person_list.append(Person("D", 1988, 73))
person_list.append(Person("E", 1995, 75))

for person in person_list:
    if person.get_year_of_birth()>1990:
        print(person.get_summary())
class Student(Person):
    def __init__(self, person_name:str, year_of_birth:int, email_id:str, student_id:str):
        super().__init__(person_name, year_of_birth)
        self.email=email_id
        self.id=student_id
    def get_summary(self):
        return f"name:{self.get_name()}, birth year:{self.get_year_of_birth()}, mail:{self.email}"
a_student=Student("G", 1999, "g@gmail", "12")
print(a_student.get_summary())
a_student.set_name("ejaz")
print(a_student.get_summary())

class Teacher(Person):
    def __init__(self,person_name: str, year_of_birth:int, department: str):
        super().__init__(person_name,year_of_birth)
        self.dept=department

    def get_summary(self):
        return f"{self.get_name()},{self.get_year_of_birth()},{self.dept}"

new_person_list=[Person("A",1989,),
                 Student("B", 1990,"f@gmail","4"),
                 Teacher("C",1980,"jkk")]
for p in new_person_list:
    print(p.get_summary())

class PlainClass:
    pass
a=PlainClass()
a.age=87
a.name="klk"
print(a.name, a.age)

    
        


