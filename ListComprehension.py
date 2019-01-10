numbers = [1,2,3,4,5,6,7,8,9,10]

# 1.a for loop example - I want 'n' for each 'n' in numbers

my_list = []
for n in numbers:
    my_list.append(n)
print(my_list)

# 1.b Comprehension - I want 'n' for each 'n' in numbers

my_list = [n for n in numbers]
print(my_list)

# 2.a for loop example - I want 'n*n' for each 'n' in numbers
my_list = []
for n in numbers:
    my_list.append(n*n)
print(my_list)

# 2.b Comprehension - I want 'n*n' for each 'n' in numbers

my_list = [n*n for n in numbers]
print(my_list)

# 3.a for loop example - I want 'n' for each 'n' in numbers if n is even
my_list = []
for n in numbers:
    if n%2 == 0:
        my_list.append(n)
print(my_list)

# 3.b Comprehension - I want 'n*n' for each 'n' in numbers

my_list = [n for n in numbers if n%2 == 0]
print(my_list)


# 4.a for loop example - I want (letter,num) for each letter in abcde and each num in 12345 
my_list = []
for letter in 'abcde':
    for num in range(5):
        my_list.append((letter,num))
print(my_list)

# 4.b Comprehension - I want (letter,num) for each letter in abcde and each num in 12345 
my_list = [(letter,num) for letter in 'abcde' for num in range(5)]
print(my_list)


# 5.a for loop example - Dictionary comprehension
fnames = ['Sachin','Sourav','Rahul','Mahendra','Virat']
snames = ['Tendulkar','Ganguly','Dravid','Dhoni','Kohli']

# Dictionary of dict = {'fname':'sname'} for each fname and sname in zip(fname,sname)
my_dict = {}
for fname,sname in zip(fnames,snames):
    my_dict[fname] = sname
print(my_dict)

# 5.b Dictionary comprehension - Remove Viart from the list
my_dict = {fname:sname for fname,sname in zip(fnames,snames) if fname != 'Virat'}
print(my_dict)

# 6.a Set Comprehensions - for loop generate squared value of a set
numbers = [1,2,3,4,5,6,7,8,6,3,2,4,5,8,1,2,8,9,2,3,5,6,5,9,10]
my_set = set()
for n in numbers:
    my_set.add(n*n)
print(my_set)

# 6.b Set Comprehensions - generate squared value of a set
my_set = {n*n for n in numbers}
print(my_set)
