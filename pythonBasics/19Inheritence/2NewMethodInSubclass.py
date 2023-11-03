class Employee():
    def do_work(self):
        print("I'm working!")

class Manager(Employee):
    def waste_time(self):
        print("Wow, this YouTube video looks fun!")

class Director(Manager):
    def fire_employee(self):
        print("You're fired!")


e = Employee()
m = Manager()
d = Director()

e.do_work()  #op: I'm working!
# e.waste_time()

m.do_work() #op: I'm working!
m.waste_time() #op: Wow, this YouTube video looks fun!
# m.fire_employee()

d.do_work() #op: Wow, this YouTube video looks fun!
d.waste_time() #op: Wow, this YouTube video looks fun!
d.fire_employee() #op: You're fired!