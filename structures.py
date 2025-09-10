"""print('Hello World')

numbers = [1,2,3, 3.4, 'Hello']

even_numbers = [2,4,6,8,10]
print(numbers.extend(even_numbers))
numbers.append(32)
print(numbers[-2])
print(numbers[2:5])
print(numbers[2:])

del numbers[3]
print(numbers)

for number in numbers:
    print(number)
"""
numbers = [number* number for number in range(1,6)]
print(numbers)

variable = (1)
print(variable)

numbers = {1: "one", 2:'two'}
numbers[3] = 'three'
print(numbers[1])
for key in numbers:
    print('key: ' , key)

student_id = {111, 111,1113,112,115}
print(student_id)

empty_set = set()
empty_set.add(32)
print(empty_set)

programmings = {'Java', 'Python', 'C++'}
print(programmings)
print(programmings.discard('Java'))

A = {1,2,3}
B = {3, 4, 5}

print('A intersection B is: ',  A.union(B))