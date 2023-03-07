## the below is used to create an empty dictionary
{}

#creating dictionary with values 
iceCreamsPreferences = {
    "benjamin" : "chocolate",
    "sandy" : "vanilla",
    "marv": "cookies & creme",
    "julia": "chocolate"
}

print(len(iceCreamsPreferences)) #op: 4

#if we pass the key twice they it will have the latest/last value as the final value
employeeSalary = {
    "employee1" : 200,
    "employee1" : 300,
    "employee2" : 400
}
print(len(employeeSalary)) #op: 2
print(employeeSalary) #op: {'employee1': 300, 'employee2': 400}   note that it picks the last values for employee1