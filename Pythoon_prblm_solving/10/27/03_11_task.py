# 1.Given two lists — one with last month’s marks and another with this month’s marks.
# print how many students improved their scores.
# Input:
# last_month_score = [45, 60, 70, 55, 80]
# this_month_score = [50, 58, 75, 65, 78]
# Output: 3
# # students number = 1, 3, and 4 are improved

a=[45,60,70,55,80]
b=[50,58,75,65,78]
count = 0
for i in range(len(a)):
    if a[i]<b[i]:
        count=count+1
        print(i)
print(count)




# 2. Convert all spaces in a given sentence into - (without using in-built functions).
# ```python
# Input: "Learn Python Easily"
# Output: "Learn-Python-Easily"
# ```

text="learn python easily"
space=""
for i in text:
    if i==" ":
        space=space+"-"
    else:
        space=space+i
print(space)


# 3. Find Index of an Element (Without using index() or any in-built methods)
# Write a program to find the index position of a given number manually using loops.
# ```python
# Input:
# numbers = [11, 22, 33, 44, 55]
# search = 33
# Output: 2

numbers=[11,22,33,44,55]
search=int(input("enter a number to search"))
for i in range(len(numbers)):
    if numbers[i]==search:
        print(i)
