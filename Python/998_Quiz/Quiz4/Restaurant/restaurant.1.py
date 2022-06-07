import random
welcome = input("Welcome to Tour Guide Central, please Select your next Eatery! Guiseppe's, Habit Burgers, Evil Shawarma, or Sabor de Fuego & many others: ")

Guiseppe_menu = ['Cheese Pizza', 'Mozarella Sticks', 'Calzone', 'Margarita Pizza', 'Special Flatbread']

Habit_menu = ['Double Double', 'Mushroom Burger', 'Cheese Melt', 'Vanilla Milkshake', 'Fries']

Shawarma_menu = ['Chicken Wrap', 'Kebab Wrap', 'Fire Wrap', 'Caesar Salad', 'Meat Plate Special'] 

Sabor_menu = ['Quesadillas', 'Sopa del Día', 'Carne Asada Burrito', 'California Special', 'Torta de Pollo']

if welcome == "Guiseppe's":
    print("Guiseppe's Menu: ")
    for i in range(0,len(Guiseppe_menu)):
        print(Guiseppe_menu[i])
    print("Today we suggest: " + Guiseppe_menu[random.randrange(0,5)]) 

elif welcome == "Habit Burgers":        
    print("Habit Burgers Menu: ")
    for i in range(0,len(Habit_menu)):
        print(Habit_menu[i])
    print("Today's Suggestion is: " + Habit_menu[random.randrange(0,5)]) 

elif welcome == "Evil Shawarma":
    print("Evil Shawarma Menu: ")
    for i in range(0,len(Shawarma_menu)):
        print(Shawarma_menu[i])
    print("Why not try?: " + Shawarma_menu[random.randrange(0,5)]) 

elif welcome == "Sabor de Fuego":
    print("Sabor de Fuego Menu: ")
    for i in range(0,len(Sabor_menu)):
        print(Sabor_menu[i])
    print("Chef's Choice: " + Sabor_menu[random.randrange(0,5)])
else:
    print("Sorry that is not available today!")
    