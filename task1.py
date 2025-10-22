fruits = ("apple", "banana", "cherry", "mango", "banana")
print(len(fruits))


find_index=fruits.index("banana")
print(find_index)


# change=fruits[2] = "grape"
# print(change) tuple can not modify values


fruits_list = list(fruits)
fruits_list[2] = "grape"
fruits = tuple(fruits_list)
print(fruits)

