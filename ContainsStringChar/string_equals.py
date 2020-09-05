# Python program to find if str2 contains all charactors from str2
str1 = "armyamq"
str2 = "maryarrmqz"

x = set(str1)
y = set(str2)
common = set(str1).intersection(str2)

if len(x) <= len(y) and len(common) == len(x):
    print("True")
else:
    print("False")