x = int(input("Please enter your first number: "))
y = input("Please enter an operation: ")
z = int(input("Please enter your second number: "))

mult = x*z
div = x/z
add = x+z
sub = x-z

if y == '*':
    print(str(x) + y + str(z) + "=" + str(mult))
elif y == '/':
    print(str(x) + y + str(z) + "=" + str(div))
elif y == '+':
   print(str(x) + y + str(z) + "=" + str(add))   
elif y == '-':
    print(str(x) + y + str(z) + "=" + str(sub))