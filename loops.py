people = ['Robin', 'Paul', 'Sara', 'Jason']

# Simple for loop

for person in people:
    print(f'Current Person: {person}') # output : Current Person: Robin
#                                                 # Current Person: Paul
#                                                 # Current Person: Sara
#                                                 # Current Person: Jason


# Break

for person in people:
    if person == 'Sara':
        break
    print(f'Current Person: {person}') # output: Current Person: Robin
#                                                # Current Person: Paul

# Continue

for person in people:
    if person == 'Sara':
        continue
    print(f'Current person is {person}') # output : Current person is Robin
                                                  # Current person is Paul
                                                  # Current person is Jason   -(skipped sara)-

# range
for i in range(len(people)):
    print(people[i]) #output : Robin
                             # Paul
                             # Sara
                             # Jason

for i in range(0, 11):
    print(f'Number : {i}') # output : Number : 0
                                    # Number : 1
                                    # Number : 2
                                    # Number : 3
                                    # Number : 4
                                    # Number : 5
                                    # Number : 6
                                    # Number : 7
                                    # Number : 8
                                    # Number : 9
                                    # Number : 10