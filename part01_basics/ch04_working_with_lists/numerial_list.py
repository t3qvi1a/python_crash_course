for value in range(1, 6):
    print(value)

numbers = list(range(2, 11, 2))
print(numbers)


squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

for number in range(1, 21):
    print(number)

for number in range(3, 31, 3):
    print(number)

numbers = [number*3 for number in range(1, 11)]
print(numbers)

numbers = [number**2 for number in range(1, 11)]
print(numbers)
