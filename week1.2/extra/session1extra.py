from collections import namedtuple, deque, Counter

fruit = ["Apple", "Banana", "Cherry", "Dragonfruit", "Grape", "Strawberry"]
new_fruit = [x for x in fruit if "r" in x]
print(fruit)
print(new_fruit)

print("\n")

numbers = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
even_numbers = {x for x in numbers if x % 2 == 0}
print(numbers)
print(even_numbers)

print("\n")

powers = {number: number**2 for number in range(1,6)}
print(powers)

print("\n")

student = namedtuple("student", ["name", "age", "dob"])
student_0 = student("Emma", "18", "5/6/2008")
print(student_0[1])
print(student_0.name)

print("\n")

dq = deque([1,2,3,4])
print(dq)
dq.appendleft(0)
print(dq)
dq.extend([6,7,8,9])
print(dq)
dq.rotate(2)
print(dq)

print("\n")

list_0 = [1,1,1,2,3,4,4,4,5,5]
print(Counter(list_0))
print(Counter(list_0).most_common(2))
