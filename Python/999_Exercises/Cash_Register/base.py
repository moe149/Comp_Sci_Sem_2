
items = int(input("How many items do you want to buy? "))
total = 0
for x in range(0,items):
    item = input("What item is this? ")
    cash = int(input("How much was this item? "))
    print("Good choice of " + item + ", Next!")
    total = total + cash
    
print("The total is: " + str(total))
print("Come again!!!")
    
    