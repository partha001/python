count = 0
while count<=5:
    print(count)
    count+=1


#this loop doesnt get executed since previous has ended with count=6
#thus condition for the below while is not satisfied in the first place 
#and the execution doesnt go into the below while loop
while count <=5:
    print(count)
    count+=1
