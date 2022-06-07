import random
welcome = input("Welcome to Tour Guide Central, please Select your next Eatery! Guiseppe's, Habit Burgers, or Evil Shawarma & many others")

Guiseppe_menu = [Cheese Pizza, Mozarella Sticks, Calzone, Margarita Pizza, Special Flatbread]

Habit_menu = [Double Double, Mushroom Burger, Cheese Melt, Vanilla Milkshake, Fries]

Shawarma_menu = [Chicken Wrap, Kebab Wrap, Fire Wrap, Caesar Salad, Meat Plate Special] 

if welcome == 'Guiseppe':
    print('Alright here are your choices' + [Guiseppe_menu])
    print('Today we suggest: ' + random.randrange[Guiseppe_menu]) 
elif welcome == 'Habit Burgers':        
    print('Alright here are your choices' + [Habit_menu])
    print('Today we suggest: ' + random.randrange[Habit_menu])
elif welcome =='Evil Shawarma':
    print('Alright here are your choices' + [Shawarma_menu])
    print('Today we suggest: ' + random.randrange[Shawarma_menu])
else:
    print("Sorry that is not available today!")
    