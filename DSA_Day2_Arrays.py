#PRACTICE OF ARRAYS AND LIST 
numbers = [5, 10, 20, 25]

numbers.sort()
print("second largest no:",numbers[-2])


numbers.insert(2, 15)
print("After insertion:", numbers)

numbers.remove(10)
print("After removal:", numbers)

numbers.pop(0)
print("after pop:",numbers)

numbers.reverse()
print("reveresed list :",numbers)

numbers = [1, 3, 5, 7, 9]
target = 12

# two pointer technique
left = 0
right = len(numbers) - 1

while left < right:
    total = numbers[left] + numbers[right]

    if total == target:
        print(numbers[left], numbers[right])
        
    elif total < target:
        left += 1
    else:
        right -= 1

numbers = [1, 2, 4, 6, 8, 10]
target = 13
left=0
right= len(numbers)-1
found = False
while left<target:
    total=numbers[left]+numbers[right]
    if total==target:
        print(numbers[left],numbers[right]) 
        found=True
        break
    elif total< target:
        left+=1
    else:
        right-=1
if not found:
    print('pair element not found ')


