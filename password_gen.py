import string
import random

minimum_length = int(input("Enter minimum length: "))
numbers_r = bool(input("Are numbers required? (True/False) "))
special_chars_r = bool(input("Are special characters required? (True/False) "))
capital_req_r = bool(input("Is a capital letter required? (True/False)  "))



def generate_password(minimum_length = 10, numbers = True, special_chars = True, capital_req = True):
    letters = string.ascii_letters
    numbers = string.digits
    special_chars = string.punctuation
    character_pool = letters


    if numbers:
        character_pool += numbers
    if special_chars:
        character_pool += special_chars

    meets_criteria = False
    number_req = False
    character_req = False
    capital_req = False
    pwd = ''
    while not meets_criteria or len(pwd)<minimum_length:
        unit = random.choice(character_pool)
        pwd += unit

        if unit in numbers:
            number_req = True
        if unit in special_chars:
            character_req = True
        if unit in letters[26:]:
            capital_req = True
        
        if numbers:
            meets_criteria = number_req
        if special_chars:
            meets_criteria = meets_criteria and character_req
        if capital_req:
            meets_criteria = meets_criteria and capital_req
        

    return pwd
site = input("Enter site name: ")
username = input("Enter username: ")
pwd = generate_password(minimum_length,numbers_r,special_chars_r,capital_req_r)
print(pwd)

with open  ("C:\\Users\\somro\\Documents\\password_database.csv",'a') as f:
    data = [site,username,pwd]
    final_data = ','.join(data)
    f.write(final_data)
    f.write('\n')


