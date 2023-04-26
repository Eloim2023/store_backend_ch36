print("test 1")


#### Dict

user = {
    "name": "Eloim",
    "last_name":"Arreola",
    "age": 42
}
print(user)
print(type(user))

print(user["name"] + " " + user["last_name"])


# INV HW: String formatting in Phyton
#f string in phyton


### List
numbers = [1,2,3]

#add
numbers.append(4)
numbers.append(5)

print(numbers)

#length
print(len(numbers)) #count items
print(len(user["name"])) #count chars
print(len(user)) # count the keys

###########

ages = [32, 74, 20, 69, 52, 26, 31, 77, 43, 73, 51, 57, 19, 79, 40, 34, 27, 23, 21, 44, 53, 55, 24, 36, 41, 47, 78, 46, 68, 75, 49, 83, 61, 60, 29, 56, 67, 17, 70, 81, 87, 38]

def exc1():
    #print all the numbers
    total = 0
    for age in ages:
        total = total + age
        ##print(age)

    print(total)


def exc2():
    #print all numbers greater or equal than 1
    # count and the print how many users area equal or older than 21

    count = 0
    for age in ages:
        if age >= 21:
            print(age)
            #count = count +1
            count += 1



def exc3():

#count how many users are between 30 and 40 years old

    count = 0
    for age in ages:
        if age >=30 and age <= 40:
            count += 1

    print("There are " + str(count) + " users between 30 and 40")

#call the functions
exc1()
exc2()
exc3()
