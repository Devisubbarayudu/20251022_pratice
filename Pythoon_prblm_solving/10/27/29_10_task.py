# print the person who got max salary
emp_name=["deviya","ramya","lethi","chithra"]
emp_sal=[2000,1500,3000,3000]
max=emp_sal[0]
for i in range(1,len(emp_sal)):
    if emp_sal[i]>max:
        max=emp_sal[i]
for i in range(len(emp_name)):
    if max==emp_sal[i]:
        print(emp_name[i])


# 1. There is an error while counting how many times a number appears in the list. Please identify and correct it.
nums = [1, 2, 3, 2, 2, 4]
target = 2
count = 0
for i in range(len(nums)):
    if nums[i] == target:
        count += 1
print(count)

# 2. There is an error while comparing two strings character by character. Please identify and correct it.
s1 = "cat"
s2 = "dog"
same = True
for i in range(len(s1)):
    if s1[i] != s2[i]:
        same == False
    elif s1[i] == s2[i]:
        same == True
        print("Same")
    else:
        print("Different")

# 3. There is an error while counting spaces in a given sentence. Please identify and correct it.
sentence = "Python is fun"
spaces = 0
for ch in sentence:
    if ch == " ":
        spaces += 1
print("Spaces:", spaces)

# 4. There is an error while finding the frequency of each character in a string. Please identify and correct it.
# text = "banana"
# for ch in text:
#     c = 0
#     for i in range(len(text)):
#         if text[i] == ch:
#             c = c + 1
#     print(c)


# 5. There is an error while counting the number of words in a given string. Please identify and correct it.
text = "I love Python"
count = 1
for ch in text:
    if ch == " ":
        count = count+1
print("Words:", count)