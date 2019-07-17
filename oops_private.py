class Member:
    '''Represents member class'''
    __privatevar = 0    #Python standard to create private var (ENFORCED using name mangling)
    _semiprivatevar = 0 #Python standard to create private var (only use in the same class) but not ENFORCED
    publicvar = 23      #Public variable
    
    def __init__(self, name):
        self.name = name
        print ('Member initialized - "{}"'.format(self.name))
    
    def tell(self):
        print ('Name:"{}"'.format(self.name))

class Student(Member):
    def __init__(self, name, marks=None):
        if not marks:
            #This works and is suggested way of naming public var
            #self.marks = Member.publicvar
            
            #This works but not suggested
            #self.marks = Member._semiprivatevar
            
            # This will fail due to python name mangling making the variable starting with __ as private
            #Detailed error here for reference
                #             PS D:\GithubRepos\Personal\PythonSamples> py .\oops_private.py
                # Traceback (most recent call last):
                #   File ".\oops_private.py", line 26, in <module>
                #     m = Student("atul")
                #   File ".\oops_private.py", line 17, in __init__
                #     self.marks = Member.__privatevar
                # AttributeError: type object 'Member' has no attribute '_Student__privatevar'
            
            self.marks = Member.__privatevar 

        else:
            self.marks = marks
        Member.__init__(self, name)
    
    def tell(self):
            Member.tell(self)
            print ('Marks:"{}"'.format(self.marks))

Member.publicvar  = 99
m = Student("atul")
Member.publicvar  = 199
m1 = Student("Gaurav")
m.tell()
m1.tell()