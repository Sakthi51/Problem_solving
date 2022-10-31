# increasing triangle
n = 5
for i in range(n):
    for j in range(i+1):
        print('*', end=' ')
    print()

print('__________')
# decreasing triangle
n = 5
for i in range(n):
    for j in range(i, n):
        print('*', end=' ')
    print()

# right sided triangle, increasing
n = 5
for row in range(n):
    for column in range(row, n-1):
        print(' ', end=' ')
    for column in range(row+1):
        print('*', end=' ')
    print()

print('__________')
# right sided triangle, decreasing
n = 5
for row in range(n):
    for column in range(row):
        print(' ', end=' ')
    for column in range(row, n):
        print('*', end=' ')
    print()

# hill pattern
n = 5
for i in range(n):
    for j in range(i, n-1):
        print(' ', end=' ')
    for j in range(i+1):
        print('*', end=' ')
    for j in range(i):
        print('*', end=' ')
    print()

# Diamond pattern
n = 5
for i in range(n-1):
    for j in range(i, n-1):
        print(' ', end=' ')
    for j in range(i+1):
        print('*', end=' ')
    for j in range(i):
        print('*', end=' ')
    print()
for i in range(n):
    for j in range(i):
        print(' ', end=' ')
    for j in range(i, n-1):
        print('*', end=' ')
    for j in range(i, n):
        print('*', end=' ')
    print()

# row constant problem
# for number patterns don't use the i and j for printing a number
# initialize a new variable 
n = 5
p = 1
for i in range(1, n+1):
    for j in range(i):
        print(p, end=' ')
    p += 1
    print()
# row constant problem
# for number patterns don't use the i and j for printing a number
# initialize a new variable
n = 5
p = 1
for i in range(1, n+1):
    for j in range(i):
        print(p, end=' ')
    p += 1
    print()

print('___________')
n = 5
p = 1
for i in range(n):
    for j in range(i+1):
        print(' ', end=' ')
    for j in range(i, n):
        print(p, end=' ')
    p += 1
    print()

# row decrementing problems
# for number patterns don't use the i and j for printing a number
# initialize a new variable
n = 5
p = 5
for i in range(n):
    for j in range(i+1):
        print(p, end=' ')
    p -= 1
    print()

# incresasing triagle
# rows odd = 1 and even = 2
n = 5
for i in range(1, n+1):
    for j in range(i):
        if i%2==0:
            print('2', end=' ')
        else:
            print('1', end=' ')
    print()

# change in column numbers
# for change in columns intialize inside the loops
n = 5
k = 5
for i in range(n):
    p = k
    for j  in range(i+1):
        print(' ', end=' ')
    for j in range(i, n):
        print(p, end=' ')
        p -= 1
    k -= 1
    print()

# floyd triangle
n = 4
p = 1
for i in range(n):
    for j in range(i+1):
        print(p, end=' ')
        p += 1
    print()
