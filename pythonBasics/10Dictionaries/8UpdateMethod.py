#the update() method merges one dictionary to another
employeeSalaries = {
    "partha" : 1000,
    "saikat": 2000,
    "anuradha": 3000
}

extraEmployeeSalaries = {
    "suvosree": 4000,
    "anuradha": 5000
}

employeeSalaries.update(extraEmployeeSalaries)
print(employeeSalaries)
#op: {'partha': 1000, 'saikat': 2000, 'anuradha': 5000, 'suvosree': 4000}
#note that for the common keys the values are overwritten

