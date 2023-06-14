##########
# NON COMPLIANT
##########

def compliant_basic_training():
    for current_weapon in ["saber_green", "saber_blue", "saber_red"]: # Noncompliant {{Use generator comprehension instead of list comprehension in for loop declaration}}
        print(current_weapon)

def non_compliant_list_training():
    for current_weapon in [weapon_number for weapon_number in range(1000)]: # Noncompliant {{Use generator comprehension instead of list comprehension in for loop declaration}}
        print(current_weapon)


##########
# COMPLIANT
##########

def compliant_basic_training():
    for current_weapon in ("saber_green", "saber_blue", "saber_red"):
        print(current_weapon)

def compliant_basic2_training():
    for current_weapon in range(10):
        print(current_weapon)

def compliant_list_training():
    for current_weapon in (weapon_number for weapon_number in range(1000)):
        print(current_weapon)
