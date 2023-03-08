concertAttendees = [
    {"name":"taylor", "section":400, "prices paid":99.99},
    {"name":"christina", "section":200, "prices paid":149.99},
    {"name":"jeremy", "section":100, "prices paid":10.99},
]


for attendee in concertAttendees:
    for key, value in attendee.items():
        print(f"the {key} is {value}")
#op:
# the name is taylor
# the section is 400
# the prices paid is 99.99
# the name is christina
# the section is 200
# the prices paid is 149.99
# the name is jeremy
# the section is 100
# the prices paid is 10.99
