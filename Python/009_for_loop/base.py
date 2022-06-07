x = int(input("Please enter line length: "))
y = input("Do you want a horizontal or vertical line? ")

if y == "vertical":
    for x in range(0, x):
        print("*")

if y == "horizontal":
    for x in range(0,x):
        print("*", end="")