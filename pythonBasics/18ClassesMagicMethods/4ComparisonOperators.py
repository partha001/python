class Student():
    def __init__(self, math, history, writing) :
        self.math = math
        self.history = history
        self.writing = writing
    
    @property
    def grades(self):
        return self.math + self.history + self.writing
    
    def __eq__(self, other_student) -> bool:
        return self.grades == other_student.grades
    
    def __gt__(self, other_student):
        return self.grades > other_student.grades
    
    def __le__(self,other_student):
        return self.grades <= other_student.grades
    
    def __add__(self, other_student):
        return self.grades + other_student.grades
    
    def __sub__(self, other_student):
        return self.grades - other_student.grades
    

bob = Student( math=90, history=90, writing=90) #270
moe = Student(math=100, history=90, writing=80) #270
joe = Student(math=40, history=45, writing=50)

print( moe > joe) #op: True
##  this will internally call the dunder gt method

print(joe <=bob) #op: True
## the above line will internally call the dunder le method


print(bob + moe) #op: 540   
## the above line will internally call the dunder add method

print(moe - joe) #op: 135
## the above line will internally call the dunder sub method

##similarly we have our own implementation of multiplying and deviding two students
