weapons_list = ['saber_green', 'saber_blue', 'saber_red']

##########
# NON COMPLIANT for "list comprehension"
##########

def non_compliant_training_1():
    for current_weapon in [weapon for weapon in weapons_list]: # Noncompliant {{Use generator comprehension instead of list comprehension in for loop declaration}}
        print(current_weapon)

def non_compliant_training_2():
    for current_weapon in [weapon_number for weapon_number in range(1000)]: # Noncompliant {{Use generator comprehension instead of list comprehension in for loop declaration}}
        print(current_weapon)


##########
# COMPLIANT for "list comprehension"
##########

def compliant_training_1():
    for current_weapon in weapons_list:
        print(current_weapon)

def compliant_training_2():
    for current_weapon in range(10):
        print(current_weapon)

def compliant_training_3():
    for current_weapon in ('saber_green', 'saber_blue', 'saber_red'):
        print(current_weapon)

def compliant_training_4():
    for current_weapon in ['saber_purple', 'saber_pink', 'saber_white']:
        print(current_weapon)

def compliant_training_5():
    for current_weapon in (weapon_number for weapon_number in range(1000)):
        print(current_weapon)
