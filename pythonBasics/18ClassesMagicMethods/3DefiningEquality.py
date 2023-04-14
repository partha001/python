#this is equals to the .equals() method in java

class Student():
    def __init__(self,math, history, writing):
        self.math = math
        self.history = history
        self.writing = writing

    @property
    def grades(self):
        return self.math + self.history + self.writing
    
    def __eq__(self, other_student):
        return self.grades == other_student.grades
    

bob = Student(math=90, history=90, writing=90)
moe = Student(math=100, history=90, writing=80)
joe = Student(math=40, history=45, writing=50)

#now checking for equality
print(bob==moe) #op: True
print(bob==joe) #op: False


#we can also check for inequality using our equality method
print(bob!=moe) #op: False
print(bob!=joe) #op: True
    