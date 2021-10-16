#Class Features
#Methods
#Initialization
#Help text

import datetime

class User:
    # init is a method function within a class 
    # init stands for initialization method
    """ Need help? Me too. """

    def __init__(self, full_name, birthday): # self is a reference to the new object tha is being created.
        self.name = full_name
        self.birthday = birthday #self.birthday is the field that stores the value
                                # birthday is the value provided when you create a user object4

        #extract first and last names
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]
    
    def age (self):
        """ Return the age of the user on years"""
        #compute the age using the users birthday

        today = datetime.date(2001, 5, 12)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm,dd) # Date of birth
        age_in_days = (today - dob).days # gets a time delta object this obejct has field called days
        age_in_years = age_in_days / 365
        return int(age_in_years)


    # calling the object
# user = User( "Jonathan Suconota", "20031209")
# print(user.name)
# print(user.birthday

#help(User)  #displays the docstring as a summary
user = User( "Jonathan Sucon", "18401209")
print(user.age())
