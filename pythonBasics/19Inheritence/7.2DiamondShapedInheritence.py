class FilmMaker():
    def give_interview(self):
        print("I love making movies!")

class Director(FilmMaker):
    pass

class Screenwriter(FilmMaker):
    def give_interview(self):
        print("I love writing scripts!")

class JackOfAllTrades(Screenwriter, Director):
    pass

stallone = JackOfAllTrades() 
stallone.give_interview() ##op: I love writing scripts!

print(JackOfAllTrades.mro()) ##op: [<class '__main__.JackOfAllTrades'>, <class '__main__.Screenwriter'>, <class '__main__.Director'>, <class '__main__.FilmMaker'>, <class 'object'>]