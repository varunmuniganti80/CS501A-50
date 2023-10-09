#CS175
#Varun sri ram muniganti
#restaurant

repeat = 'yes'
while repeat == 'yes':

    
    Vegetarian = False
    Vegan = False
    Gluten_free = False


    choice1 = input("Is anyone in your party Vegetarian?" ).lower()
    choice2 = input("Is anyone in your party Vegan?" ).lower()
    choice3 = input("Is anyone in your party Gluten_free?" ).lower()

    if choice1 == 'yes':
        Vegetarian = True
    if choice2 == 'yes':
        Vegan = True
    if choice3 == 'yes':
        Gluten_free = True

    if Vegetarian == False and Vegan == False and Gluten_free == False:
     print("Joe's Gourment Burgers,Main Street Pizza Company,Corner Café,Mama's Fine Italian, The Chef’s Kitchen")
    elif Vegetarian == True and Vegan == False and Gluten_free == False:
     print(" Main Street Pizza Company, Corner Café, Mama's Fine Italian,The Chef’s Kitchen")
    elif Vegetarian == False and Vegan == False and Gluten_free == True:
     print(" Main Street Pizza Company, Corner Café, The Chef’s Kitchen")
    elif Vegetarian == True and Vegan == False and Gluten_free ==True:
     print("Main Street Pizza Company, Corner Café, The Chef’s Kitchen")
    elif Vegetarian == False and Vegan == True and Gluten_free == False:
     print("Corner Café, The Chef’s Kitchen")
    elif Vegetarian == False and Vegan == True and Gluten_free == True:
     print("Corner Café, The Chef’s Kitchen")
    elif Vegetarian == True and Vegan == True and Gluten_free == False:
     print("Corner Café, The Chef’s Kitchen")
    elif Vegetarian == True and Vegan == True and Gluten_free == True:
     print("Corner Café, The Chef’s Kitchen")

    else:
         print("sorry!")

repeat = input("do you want to continue")
