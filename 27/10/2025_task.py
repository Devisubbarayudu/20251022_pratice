# 1. Problem: Given an array of integers, count how many numbers are even and how many are odd.
# Example Input: [1, 2, 3, 4, 5, 6]
# Example Output: { even: 3, odd: 3 }
a=[1,2,3,4,5,6]
even=0
odd=0
for i in range(len(a)):
    if a[i]%2==0:
        even=even+1
    else:
        odd=odd+1
print("even numbers count:",even)
print("odd number count",odd)


# 3. Given a string, the task is to reverse the order of the words in the given string.
# Examples:
# Input: s = “hello everyone”
# Output: s = “everyone hello”
# Input: s = “i love programming very much”
# Output: s = “much very programming love i”
s="hello world"
reversed=s.split(" ")
reversed_str=reversed[::-1]
sentence=" ".join(reversed_str)
print(sentence)


# 2. Problem: Given an array of integers and a target element, find the indices of its first and last occurrence.
# Example Input: ([5, 2, 3, 5, 7, 5, 8], 5)
# Example Output: { firstIndex: 0, lastIndex: 5 }
a=[5,2,3,5,7,5,8]
find=int(input("enter the number to find"))
first=0
last=0
for i in range(len(a)):
    if a[i]==find:
        first=i
        break
for j in range(len(a)):
    if a[j]==find:
        last=j