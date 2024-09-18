from person import Person
from employee import Employee

class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."
    
A = Teacher()
print(A.sleep())
print(A.get_fired())
print(A.teach())