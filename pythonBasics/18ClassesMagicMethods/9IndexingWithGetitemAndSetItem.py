# pillows = {
#     "soft": 79.99,
#     "hard": 99.99
# }

# print(pillows["soft"])
## the above line internally works as below
# print(pillows.__getitem__("soft"))

class CrayonBox():
    def __init__(self):
        self.crayons = []

    def add(self, crayon):
        self.crayons.append(crayon)

## implementing our own getitem and setitem method
## thus the below fetch item by index works . and will fail to work if we comment the below 2 method implementations
    def __getitem__(self, index):
        return self.crayons[index]

    def __setitem__(self, index, value):
        self.crayons[index] = value


cb = CrayonBox()
cb.add("Blue")
cb.add("Red")

## accessing the values by index internally calls our custom __getitem method
print(cb[0])
print(cb[1])

## similarly setting value by index internally calls our custom implmentation of __setitem method
cb[0] = "Yellow"

print(cb[0])

for crayon in cb:
    print(crayon)