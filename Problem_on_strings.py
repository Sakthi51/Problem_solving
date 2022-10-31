# Python Program for checking a character is a vowel or consonant
vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I' 'O', 'U']
letter = input('Enter a alphabet: ')
if letter in vowel:
    print('Vowel')
else:
    print('Consonant')

# alternative method
char = input()
if char in 'aeiouAEIOU':
    print('vowel')
else:
    print("consonant")

# Check whether a character is a alphabet or not
char = input()
if  ord(char)>=97 and ord(char)<=122 or ord(char)>=65 and ord(char)<=90:
    print('alphabet')
else:
    print('not alphabet')

char = input()
if char.isalpha():
    print('alphabet')
else:
    print('not alphabet')

# Toggle each character in a string
string = 'Sakthi IS a Programmer'
new_string = ''
for i in string:
    if i.isupper()==True:
        new_string = new_string+i.lower()
    else:
        new_string = new_string+i.upper()
print(new_string)

print(string.swapcase())

# Count the number of vowels
string = 'Sakthi IS a Programmer'
vowels = 'aeiouAEIOU'
vowels_count = 0
for i in string:
    if i in vowels:
        vowels_count += 1
print(vowels_count)
    

# Python program to remove the vowels from a string
string = 'Sakthi IS a Programmer'
vowels = 'aeiouAEIOU'
for i in vowels:
    if i in vowels:
        string = string.replace(i, '')

print(string)


# reverse a string
string = 'sakthi'
string_list = [i for i in string]
reversed_string = []
for i in string_list:
    reversed_string.insert(0, i)
print(''.join(list(reversed_string)))


# Remove all characters from string except alphabets
string = 'Sakthi1711231@gmail.com'
for i in string:
    if i.isalpha():
        pass
    else:
        string = string.replace(i, '')
print(string)


string_with_only_characters = []
for i in string:
    if i.isalpha():
        string_with_only_characters.append(i)
print(''.join(string_with_only_characters))

# Remove spaces from a string
string = 'sakthi is a good programmer'
for i in string:
    if i==' ':
        string = string.replace(' ', '')
print(string)


string = string.replace(' ', '')
print(string)


# Remove brackets from an algebraic expression
# brackets = ['(', ')'] use it for (for loop)
string = "(a-b)+[c*d]+{e/f}"
bracets = ['(', ')', '{', '}', '[', ']']
brackets_removed = []

# code only one type of brackets
string = string.replace('(', '').replace(')', '')
print(string)

# for all three brackets
for i in string:
    if i not in bracets:
        brackets_removed.append(i)
print(''.join(brackets_removed))

# Count the sum of numbers in a string
string = 'Daya123Ben456'
number_count = 0
for i in string:
    if i.isalpha():
        pass
    else:
        number_count = number_count + int(i)
print(number_count)

number_count = 0
for i in string:
    if i.isnumeric():
        number_count = number_count + int(i)
print(number_count)

# Capitalize the first and last character of each word of a string
string = 'sakthi'
string = string.replace(string[0], string[0].upper())
string = string.replace(string[-1], string[-1].upper())
print(string)

for i in range(len(string)):

    if i==0:
        string = string.replace(string[i], string[i].upper())
    elif i==len(string)-1:
        string = string.replace(string[i], string[i].upper())

print(string)

# Calculate frequency of characters in a string
from collections import Counter
string = 'sakthisakthi'
string_list = [i for i in string]
string_set = set(string_list)
unique_strings = list(sorted(string_set))
for i in unique_strings:
    count = Counter(string)
    print(f'{i} occured {count[i]} times')

# Calculate frequency of characters in a string
string = 'sakthisakthi'
string_list = [i for i in string]
length = len(string_list)
frequency = [1]*length
for i in range(length):
    if frequency[i]==1: # duplicate elements won't enter
        for j in range(i+1, length):
            if string_list[i] == string_list[j]:
                frequency[i] += 1
                frequency[j] = 0  # so, duplicate eleents become zero it wil be helful the loop
for i in range (len(frequency)):
    if frequency[i]>0:
        print(f'{string_list[i]} occurs {frequency[i]}')


# Python program to find non repeating characters in a string
string = "prepinsta"

for i in string:
    count = 0
    for j in string:
        if i == j:
            count += 1
        #if count>1:  # no need in code only to decrease redundancy
        #    break
    if count==1:
        print(i, end='')



frequency = [1]*len(string)
for i in range(len(string)):
    if frequency[i]==1:
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                frequency[i] += 1
                frequency[j] = 0
    print(f'{string[i]} occurs {frequency[i]}')
print(frequency)
for i in range(len(frequency)):
    if frequency[i]==1:
        print(string[i], end='')


#Check if two strings are Anagram or not
string1 = 'silent'
string2 = 'listen'
string1 = [i for i in string1]
string2 = [j for j in string2]
string1.sort()
string2.sort()
if string1 == string2:
    print('Anagram')
else:
    print('Not anagram')
# using sorted 
string1 = sorted(string1)
string2 = sorted(string2)
if string1==string2:
    print('Anagram')
else:
    print('Not anagram')

# Python program to replace a substring in a string
# it works only for after words not for prefix words
string1 = 'hello hi'
change = 'hi'
change_with = 'hey'
for i in range(len(string1)):
        if change[0] == string1[i]:
            if string1[i:i+len(change)]==change:
                print(string1[:i]+change_with)


# using replace
# it works for both
print(string1.replace(change, change_with))
