#removing the repeted numbers in list 
numbers=[2,3,2,5,3,7,9,10]
unique=[]

for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)


#h ow many time repede number 
numbers = [2, 3, 2, 5, 3, 2]
frequency = {}
for number in numbers:
    if number in frequency :
        frequency[number]+=1
    else:
        frequency[number]= 1
print(frequency)

