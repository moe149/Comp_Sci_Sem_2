import datetime
import random

people = ["mom", "dad", "brother", "grandma", "grandpa"]
compliment = ["is cool" , "is strong", "a motivator", "is fantastic", "is a great cook"]

numberpeople = random.randrange(0,len(people))
numbercompliment = random.randrange(0,len(compliment))

print(people[numbercompliment] + " " + compliment[numbercompliment])








with open('People.txt') as f:
    for line in f:
        l = line.strip()
        for x in range (0,12):
            people.append(l)
with open('Compliment.txt') as f:
    for line in f:
        l = line.strip()
        for f in range (8):
            compliment.append(l)


#x = datetime.datetime.now()

#print()
#print("The date and time are:")
#print(str(x.day) + "/" + str(x.month) + "/" + str(x.year) + " at " + str(x.hour))

#f.close()
