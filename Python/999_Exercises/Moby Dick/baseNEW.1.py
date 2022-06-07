sentence = "whale hello there. Don't we all love whales? I absolutely love whales! whales are so huge!!!"

whale = sentence[0:len(sentence)]
x=0
y=0
for i in range(0,len(sentence)):
    x= x+1
    if sentence[i:x+4] == "whale":
        y=y+1
print("There are "+  str(y) + " whales in this line")        
    

x = 0
y = 0
with open('moby.txt') as f:
    for line in f:
        sentence = line.strip()
        for i in range(0,len(sentence)):
            x = x+1
            if sentence[i:x+4] == "whale":
                y = y+1
                print(x)
        print("There are " + str(y) + " whales mentioned in this book!")

f.close()
