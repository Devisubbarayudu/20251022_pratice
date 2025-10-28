# 1. There is an error while reversing the given string. Please identify and correct it.
word = "Python"
rev = ""
for i in range(len(word)-1,-1,-1):
    rev = rev + word[i]
print("Reversed:", rev)

# # 2. There is an error while counting vowels in the given text. Please identify and correct it.
text = "education is strength for my life"
count = 0
for ch in text:
    if ch == "a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
        count = count + 1
print("Vowels:", count)

# # 3. There is an error while finding the smallest element in the list. Please identify and correct it.
nums = [9, 5, 3, 8]
max_num = nums[0]
for i in range(1, len(nums)-1):
    if nums[i] > max_num:
        min_num = nums[i]
print(max_num)

# nums = [9, 5, 3, 8]
min_num = nums[0]
for i in range(1, len(nums)-1):
    if nums[i] < min_num:
        min_num = nums[i]
print(min_num)

# # 4. There is an error while printing alternate elements from the list. Please identify and correct it.
lst = [10, 20, 30, 40, 50, 60, 70]
for i in range(0,len(lst)):
    if i % 2 == 0:
        print(lst[i])

# # 5. There is an error while replacing negative numbers in the list with 0. Please identify and correct it.
nums = [-3, 5, -2, 7]
for n in range(0,len(nums)):
    if nums[n] < 0:
        nums[n] = 0
print(nums)
