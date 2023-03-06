countries = "india,usa,canada,germay"

print(countries.split(",")) #op: ['india', 'usa', 'canada', 'germay']
#note how the split returns a list


#passing an additional parameter we can optionally mention how man chunks we want to split
print(countries.split(",",2)) #op: ['india', 'usa', 'canada,germay']

sentence = "I am learning how to code with python"
#the split method will throw value error if we dont pass any argument
#words = sentence.split("") #op: ValueError: empty separator
words = sentence.split(" ") #op: ValueError: empty separator
print(words) #['I', 'am', 'learning', 'how', 'to', 'code', 'with', 'python']

