#prime factors
num = 630
prime_factors = []
divisor = 2
while divisor<=num:
    if num%divisor==0:
        prime_factors.append(divisor)
        num = num/divisor
    else:
        divisor = divisor+1
        
print(prime_factors)

#frequency of numbers in arrays
from collections import Counter
arr = [2, 8, 5, 2, 5, 9, 8, 2]
arr_set = set(arr)
arr_set_list = list(arr_set)
arr_set_list.sort()
for i in arr_set_list: # count only the unique elements in the list
    count = Counter(arr)
    print(f'{i} has occured {count[i]} times')

#using dictionaries
arr = [2, 8, 5, 2, 5, 9, 8, 2]
count = {}
for i in arr:
    if i in count:
        count[i] = count[i]+1
    else:
        count[i]=1
print(count)

# using frequency

arr = [1, 2, 3, 1, 2, 3]
length = len(arr)
frequency = [1]*length
for i in range(length):
    if frequency[i]==1:
        for j in range(i+1, length):
            if arr[i]==arr[j]:
                frequency[i] += 1
                frequency[j] = 0
    print(f"{arr[i]} occurs {frequency[i]}")

arr = [1, 2, 3, 1, 2, 3, 1]
frequecy = [1]*len(arr)
for i in range(len(arr)):
    if frequecy[i]==1:
        for j in range(i+1, len(arr)):
            if arr[i]==arr[j]:
                frequecy[i] += 1
                frequecy[j] = 0
# print(frequecy)
for i in range(len(frequecy)): # to avoid reapeted elements
    if frequecy[i]>0:
        print(f'{arr[i]} occurs {frequecy[i]} times')

#Sorting elements of an array by frequency
arr = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 5, 5, 5, 4, 4, 4, 4, 4, 4]
print("Initial list: ", str(arr))
result = sorted(arr, key=arr.count, reverse=True)
print(result)

#Find the Longest Palindrome in an Array using Python
arr = [1, 232, 5545455, 909090, 161]
palindrome = []
print(arr)
for ele in arr:
    if ele!=0:
        ele=str(ele)
        rev_ele=ele[::-1]
        if ele==rev_ele:
            print(f'{ele}: Palidrome')
            palindrome.append(ele)
        else:
            print(f'{ele}: Not palindrome')
palindrome.sort()
print(f'The longest palidrome is {max(palindrome)}')


# counting distinct elements
arr = [10, 20, 40, 30, 50, 20, 10, 20]
arr = set(arr)
arr = list(arr)
arr.sort()

# print(arr)
for i in arr:
    print(i, end=' ')

# using two loops
arr = [10, 20, 40, 30, 50, 20, 10, 20]
lenght = len(arr)
frequency = [1]*len(arr)
for i in range(lenght):
    if frequency[i]==1:
        for j in range(i+1, lenght):
            if arr[i]==arr[j]:
                frequency[i]+=1
                frequency[j]=0
    print(f'{arr[i]} occurs {frequency[i]}')
for i in range(len(frequency)):
    if frequency[i]>0:
        print(arr[i])

# Find maximum product sub-array in a given array
arr = [2, 3, -2, 4]
max_product = arr[0]
for i in range(len(arr)):
    product = arr[i]
    for j in range(i+1, len(arr)):
        product = product*arr[j]
        max_product = max(product, max_product)
print(max_product)


# disjoint adnd intersection
arr1 = [5, 4, 6, 7]
arr2 = [3, 2, 1]
disjoint = []
intersection = []
for i in arr1:
    for j in arr2:
        if i == j:
            intersection.append(i)
        else:
            disjoint.append(i)
            disjoint.append(j)
disjoint = (list(set(disjoint)))
print(disjoint)
print(intersection)
if len(intersection) == 0:
    print('disjoint')
else:
    print('intersected elements are: ', intersection)

# Array two is a subset of array one
arr1 = [4, 55, 66, 92, 78]
arr2 = [7, 9, 20, 145, 7, 9, 8]
intersection = []
for i in arr1:
    for j in arr2:
        if i == j:
            intersection.append(i)
print(intersection)
if set(intersection) == set(arr2):
    print('Array two is a subset of array one')
else:
    print('Array two is not a subset of array one')


# Check if all the numbers of array can be made equal
arr = [2, 2, 2]
equals = []
for i in range(len(arr)):
    while arr[i]%2 == 0:
        arr[i] //= 2
    while arr[i]%3 == 0:
        arr[i] //= 3
for i in range(len(arr)):
    if arr[0] == arr[i]:
        equals.append(1)
    else:
        equals.append(0)
print(equals)
if sum(equals)==3:
    print('array can be converted into equal')
else:
    print('array cannot be converted into equal')


# Array element with minimum sum of absolute differences
arr = [1, 3, 9, 6, 3]
absolute_difference = []
arr = sorted(arr)
median_ele = len(arr)//2
temp= arr[median_ele-1]
for i in range(len(arr)):
    arr[i] = arr[i]-temp
    if arr[i]<0:
        arr[i] = arr[i]*(-1)
    absolute_difference.append(arr[i])
print(sum(absolute_difference))

# Sum of minimum absolute difference of each array element
arr = [4, 1, 5]
arr = sorted(arr)
n = len(arr)
sum = 0
sum += abs(arr[0]-arr[1])       # first element
sum += abs(arr[n-1]-arr[n-2])   # last element
for i in range(1, n-1):
    sum += min(abs(arr[i]-arr[i-1]),
               abs(arr[i]-arr[i+1]))
print(sum)


#Sort an array based on order defined by another array
arr1 = [5, 8, 9, 3, 5, 7, 1, 3, 4, 9, 3, 5, 1, 8, 4]
arr2 = [3, 5, 7, 2]
arr1 = sorted(arr1)
print(arr1)
common_elements = [i for i in arr1 if i in arr2]
disjoint_elements = [i for i in arr1 if i not in arr2]
print(common_elements)
print(disjoint_elements)
common_elements.extend(disjoint_elements)
print(common_elements)


# Python Program to Replace each element by its Rank in the given Array
arr1 = [100, 2, 70, 12, 90]
rank = []
arr1_sorted = sorted(arr1)
for i in range(len(arr1)):
    for j in range(len(arr1_sorted)):
        if arr1[i]==arr1_sorted[j]:
            rank.append(j+1)
print(rank)


# Equilibrium Index of an Array
arr = [-7, 1, 5, 2, -4, 3, 0]
flag = 0
for i in range(len(arr)):
    leftsum = 0
    rightsum = 0
    for j in range(i):
        leftsum = leftsum+arr[j]
    for j in range(i+1, len(arr)):
        rightsum = rightsum+arr[j]
    if leftsum == rightsum:
        flag = 1
        break
if flag == 1:
    print(f'{i} is the index')
else:
    print('No index')

# using sum
arr = [1, 2, -2, -1]
ans = -1
for i in range(1, len(arr)):
    if sum(arr[:i]) == sum(arr[i+1:]):
        ans = i
        break
if ans==-1:
    print('no index found')


# left rotation and right rotation

arr = [10, 20, 30, 40, 50, 60, 70]
n = len(arr)
right_rotation_count = 1
left_rotation_count = 2
print('Original_array        :', arr)
# Right rotation
for i in range(right_rotation_count):
    last_element = arr[len(arr)-1]
    arr.insert(0, last_element)
    arr.pop()
    print(f'Array after {i+1} right rotation: {arr}')

# left rotation
for i in range(left_rotation_count):
    first_element = arr[0]
    arr.insert(len(arr), first_element)
    arr.pop(0)
    print(f'Array after {i+1} left rotation: {arr}')

#Check for balanced parentheses in Python
open_list = ['[', '{', '(']
close_list = [']', '}', ')']
string = '[{}{}(]'
stack = []
for i in string:
    if i in open_list:
        stack.append(i)
    if i in close_list:
        position = close_list.index(i)
        if len(stack)>0 and (open_list[position]==stack[len(stack)-1]):
            stack.pop()
        else:
            print('unbalanced')
if len(stack)==0:
    print('balanced')



