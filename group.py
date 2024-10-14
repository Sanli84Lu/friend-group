"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {}

Jill = {'name':'Jill', 'age':'26', 'job':'biologist',
            'connections':{'friend':['Zalika'],
                           'partner':['John']}
            }

Zalika = {'name':'Zalika', 'age':'28', 'job':'biologist',
            'connections':{'friend':['Jill']}
            }

John = {'name':'Jhon', 'age':'27', 'job':'writer',
            'connections':{'partner':['Jill']}
            }

Nash = {'name':'Nash', 'age':'34', 'job':'chef',
            'connections':{'cousin':['Jhon'],
                           'landlord':['Zalika']}
            }

my_group['Jill'] = Jill
my_group['Zalika'] = Zalika
my_group['John'] = John
my_group['Nash'] = Nash

# Maximum age of people in the group
max_age = max(person['age'] for person in my_group.values())
print(f"The maximum age of people in the group: {max_age}")

# Average (mean) number of relations among members of the group
avg_relations = sum(len(person['connections']) for person in my_group.values()) / len(my_group)
print(f"The average number of relations among members: {avg_relations:.2f}")

# Maximum age of people with at least one relation
max_age_with_relation = max(person['age'] for person in my_group.values() if len(person['connections']) > 0)
print(f"The maximum age of people with at least one relation: {max_age_with_relation}")

# [Advanced] Maximum age of people with at least one friend
max_age_with_friend = max(person['age'] for person in my_group.values() if 'friend' in person['connections'])
print(f"The maximum age of people with at least one friend: {max_age_with_friend}")