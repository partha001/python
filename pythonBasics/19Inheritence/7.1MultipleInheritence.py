class Restaurant():
    def make_reservation(self, party_size):
        print(f"Booked a table for {party_size}")

class Steakhouse(Restaurant):
    pass

class Bar():
    def make_reservation(self, party_size):
        print(f"Booked a lounge for {party_size}")

class BarAndGrill(Steakhouse, Bar):
    pass

bag = BarAndGrill()
bag.make_reservation(2) ##op: Booked a table for 2
print(BarAndGrill.mro()) ##op: [<class '__main__.BarAndGrill'>, <class '__main__.Steakhouse'>, <class '__main__.Restaurant'>, <class '__main__.Bar'>, <class 'object'>]