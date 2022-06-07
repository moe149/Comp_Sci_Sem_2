number_list = [] 
numbin = int(input('How many numbers do you want?'))
for i in range (0,numbin):
   numin = int(input('Enter your numbers: '))
   number_list.append(numin)
   
av = 0
tot = 0
maximum = 0
minimum = 1000000

for i in range (0,len(number_list)):
    tot = tot + number_list[i]
    if number_list[i] > maximum:  
        maximum = number_list[i]
    if number_list[i] < minimum:
        minimum = number_list[i]

av = tot/len(number_list)
print('Your minimum is: ' + str(minimum))
print('Your maximum is: ' + str(maximum))
print('The average is: ' + str(av))