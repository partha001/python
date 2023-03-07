pokemon = {
    "fire" : ["charmander", "charmeleon","charizard"],
    "water" : ["squirtle","warturtle","blastoise"],
    "grass" : ["bulbasaur","venusaur","ivysaur"]
}

# checking if a key exists or not 
print("fire" in pokemon) #op: True
print("Fire" in pokemon) #op: False   since they keys are case-sensitive

print("zombie" not in pokemon) #op: True
print("Fire" not in pokemon) #op: True


#previously we have seen that using [] to access values gives error if the
# key doesnt exist. well this can be handles using the get() we have seen earlier.
# however another way to make our program fail-safe if the key doesnt exist is by using
# they 'in' clause as mentioned below  
if( "zombie" in pokemon):
    print(pokemon["zombie"])
else:
    print("key doesnt exist")
#op: key doesnt exist