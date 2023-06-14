def non_compliant_list_training():
    for current_weapon in [weapon_number for weapon_number in range(1000)]: # Noncompliant {{Use generator comprehension instead of list comprehension in for loop declaration}}
        print(current_weapon)

def non_compliant_enumerate_training():
    for idx, current_weapon in enumerate([weapon_number for weapon_number in range(1000)]): # Noncompliant {{Use generator comprehension instead of list comprehension in for loop declaration}}
        print(current_weapon)

def non_compliant_zip_training():
    for current_weapon, current_weapon2 in zip([weapon_number for weapon_number in range(1000)], [weapon2_number for weapon2_number in range(1000)]): # Noncompliant {{Use generator comprehension instead of list comprehension in for loop declaration}} {{Use generator comprehension instead of list comprehension in for loop declaration}}
        print(current_weapon)

def compliant_basic_training():
    for current_weapon in range(10):
        print(current_weapon)

def compliant_filter_training():
    for current_weapon in filter(lambda weapon_number: weapon_number > 2, range(100)):
        print(current_weapon)

def compliant_list_training():
    for current_weapon in (weapon_number for weapon_number in range(1000)):
        print(current_weapon)

def compliant_enumerate_training():
    for idx, current_weapon in enumerate(range(1000)):
        print(current_weapon)

def compliant_zip_training():
    for current_weapon, current_weapon2 in zip((weapon_number for weapon_number in range(3)), ["saber_green", "saber_blue", "saber_red"]):
        print(current_weapon)
