class Person():
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __len__(self):
        return self.height

values = [
    "Boris",
    [1, 2, 3],
    (4, 5, 6, 7),
    { "a": 1, "b": 2},
    Person(name = "Boris", height = 71)
]

for value in values:
    print(len(value))

## note how the __len__ function exhibits different behavior depending upon the types of item passed to it.
## output:
# 5
# 3
# 4
# 2
# 71
