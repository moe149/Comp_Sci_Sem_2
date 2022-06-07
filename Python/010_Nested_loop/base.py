inp = input("What symbol would you like to use? ")
y = int(input("What's the width of your box? "))
z = int(input("What's the height of your box? "))

for x in range(z):
    print(" ")
    for x in range(y):
        print(inp, end="")