class SchoolMember:
    '''Represents school member'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Instantiated SchoolMember: {})'.format(self.name))

    def tell(self):
        '''Tell method'''
        print('Name:"{}" Age: "{}"'.format(self.name, self.age))

class Teacher(SchoolMember):
    '''Represents Teacher'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary
        print('Initialized Teacher: {}'.format(self.salary))
    
    def tell(self):
        SchoolMember.tell(self)
        print ('Salary: "{:d}"'.format(self.salary))


class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print ('(Initialized Student: {}) '.format(self.name))
    
    def tell(self):
        SchoolMember.tell(self)
        print ('Marks: "{:d}"'.format(self.marks))

t = Teacher("Satish", 35, 3500)
s = Student("Atul", 31, 67)

members = [t, s]
for member in members:
    member.tell()
