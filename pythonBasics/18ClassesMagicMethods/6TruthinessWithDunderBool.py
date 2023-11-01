class Emotion():
    def __init__(self, positivity, negativity):
        self.positivity = positivity
        self.negativity = negativity

    def __bool__(self):
        return self.positivity > self.negativity
    
myEmotionalState = Emotion(positivity=50, negativity=75)

if myEmotionalState:
    print("this will NOT print because I have more negativity than positivity")

myEmotionalState.positivity = 100

if myEmotionalState:
    print("this WILL print because I have more positivity than negativity")
# this WILL print because I have more positivity than negativity #output
