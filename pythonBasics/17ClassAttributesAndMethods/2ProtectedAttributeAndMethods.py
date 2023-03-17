class SmartPhone():
    def __init__(self):
        self._company = "Apple"
        self._firmware = 10.0

    def get_os_version(self):
        return self._firmware

    def update_firmware(self):
        print("Reaching out to the server for the next version")
        self._firmware += 1

iphone = SmartPhone()
print(iphone._company) #op: Apple
print(iphone._firmware) #op: 10.0

print(iphone.update_firmware()) #op: None 
print(iphone._firmware) #op: 11.0

#it is convention to name the private attributes with names starting with _ . 
#note starting an attribute name with _ doesnt actually make it private. 
# user can still access and change its value as usual as there is no concept of private or protected as such in python . 
# however starting the name with _ we are suggesting that its value should not be changed
iphone._company = "samsung"
print(iphone._company)

