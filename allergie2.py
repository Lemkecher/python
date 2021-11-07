# determine allergie

def allergie(aller):
    listofallergies = {'eggs': 1, 'peanuts': 2, 'shellfish': 4, 'strawberries': 8,
                       'tomatoes': 16, 'chocolat': 32, 'pollen': 64, 'cats': 128}
    for key, value in listofallergies.items():
        if value == aller:
            return 'You are allergic to ', key
    return None
print(allergie(4)) 
    