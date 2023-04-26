users = [
    {
        'id': 1,
        'name': 'Alice',
        'gender': 'female',
        'age': 25,
        'preferred_color': 'blue'
    },
    {
        'id': 2,
        'name': 'Bob',
        'gender': 'male',
        'age': 35,
        'preferred_color': 'GREEN'
    },
    {
        'id': 3,
        'name': 'Charlie',
        'gender': 'male',
        'age': 45,
        'preferred_color': 'Red'
    },
    {
        'id': 4,
        'name': 'Danielle',
        'gender': 'female',
        'age': 30,
        'preferred_color': 'YelloW'
    },
    {
        'id': 5,
        'name': 'Evelyn',
        'gender': 'female',
        'age': 20,
        'preferred_color': 'PuRplE'
    },
    {
        'id': 6,
        'name': 'Frank',
        'gender': 'male',
        'age': 28,
        'preferred_color': 'purple'
    },
    {
        'id': 7,
        'name': 'Grace',
        'gender': 'female',
        'age': 31,
        'preferred_color': 'GREEN'
    },
    {
        'id': 8,
        'name': 'Henry',
        'gender': 'male',
        'age': 40,
        'preferred_color': 'BLUE'
    },
    {
        'id': 9,
        'name': 'Isabelle',
        'gender': 'female',
        'age': 27,
        'preferred_color': 'red'
    },
    {
        'id': 10,
        'name': 'Jack',
        'gender': 'male',
        'age': 24,
        'preferred_color': 'yellow'
    }
]

#logic 

def exc1():
    #print all the names
    for user in users:
        print(user["name"])



def exc2(): 
    #print how many females and males we have
    females = 0
    males = 0
    for user in users:
        gender = user ["gender"]
        if gender == "female":
            females += 1
        elif gender == "male":
            males += 1

    #print("There are " + str(females) + " females and " + str(males) + " males")
    print(f"There are {females} females and {males} males")


def find_by_id(id):
    #find the user with matching id and print the entire user (dictionary)
    for user in users:
        if user ["id"] == id:
            print(user)




#call fns
exc1()
exc2()

find_by_id(3)
find_by_id(5)





