# fruits = ['apple', 'banana', 'pineapple']
# message = f"My favorite fruit is {fruits[0].title()}."
#
# print(fruits)
# fruits[1] = "watermelon"
# print(fruits)
# fruits.append("mango")
# print(fruits)
#
# print(fruits[2].upper())
# print(message)


# append
fruits = []
fruits.append("apple")
fruits.append("banana")
fruits.append("mango")
fruits.append("apple")
print(fruits)
print(sorted(fruits))

# insert
fruits.insert(-1, "watermelon")
print(fruits)

# delete: not get the value
del fruits[]
print(fruits)


# # pop: get the value
# poped_fruit = fruits.pop(0)
# print(f"poped fruit is: {poped_fruit}")
# print(f"the remaining fruits are: {fruits}")
#
# # remove: use the value to search
# # fruits.remove('mango')
# print(fruits)
#
# # sort
# fruits.append("purple")
# fruits.append("orange")
# print(fruits)
# print(sorted(fruits))
#
# fruits.sort()
# print(fruits)
#
# fruits.sort(reverse = True)
# print(fruits)
#
# fruits.reverse()
# print(fruits)
#
# print(len(fruits))
