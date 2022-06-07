import random   
inp = int(input("How many numbers do you want? "))
numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
for x in range (inp):
    print(numlist[int(random.randrange(10))], end= " ")
