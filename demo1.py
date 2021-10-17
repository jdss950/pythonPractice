#print("Hello world")

class User:
    pass   # a line that does nothing
user1 = User() # user 1 is an "instance" of the User 
                # user is an "object"

user1.first_name = "Jonathan"      # fields: Data attached to an object
user1.last_name = "Suconota"   # not capilize the words in the fields use space for more than one space.

print(user1.first_name)
print(user1.last_name)

first_name = "Jake"
last_name = "Guru"
print( first_name, last_name)   
# with classes there is no limit to the number of objects you can use.


user2 = User()
user2.first_name = "Kobe"
user2.last_name = "Kome"
print(user2.first_name,user2.last_name)
#each obejct can have different variables for the same variable names.

user1.age = 37
user2.age = 45

print( user1.age, user2.age)

#Class Features
#Methods
#Initialization
#Help text

