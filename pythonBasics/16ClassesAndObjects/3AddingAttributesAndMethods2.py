class Guitar():
    def __init__(self,wood) :
        self.wood = wood

acoustic = Guitar("Alder")
electric = Guitar("Mahogany")

print(acoustic.wood) #op: Alder
print(electric.wood) #op: Mahogany