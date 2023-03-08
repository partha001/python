collegeCourses = {
    "history":"mr.washington",
    "math":"mr.newton",
    "science":"mr.einsteing"
}

for course, professor in collegeCourses.items():
    print(f"the course {course} is being taught by {professor} .")
#op:
# the course history is being taught by mr.washington .
# the course math is being taught by mr.newton .
# the course science is being taught by mr.einsteing .

#now lets say am not interested in the keys but only the values . then we can write it as below 
for _,professor in collegeCourses.items():
    print(f"the next professor is {professor}")
#op:
# the next professor is mr.washington
# the next professor is mr.newton
# the next professor is mr.einsteing

#note that the item() returns an iterable of tuples