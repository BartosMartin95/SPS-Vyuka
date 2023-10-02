# 1 Variables
str1 = "O"
float2 = 3.1415
str3 = "nion"
none = None

word = str1 + " " + str(float2) + " " + str3
print(word)

none_to_bool = bool(none)
print(none_to_bool)

# 2-3 Lists, sets and methods
list1 = [1, 4, 5, 6, 5, 2, 3, 4, 4, "a", "z"]

set1 = set(list1)
list2 = list(set1)
print(list2)

list2.pop()
list2.pop()
print(list2)

# 4 Dictionaires
dict1 = {"student": "Alex", "age": 12, "favourite meals": None}

dict1["favourite meals"] = ["burger", "pizza"]
print(dict1["favourite meals"][0])

# 5 For and if
# for i in <3-16> print every even number
for i in range(3, 17):
    if i % 2 == 0:
        print(i)

# 6 While counter
i = 0
while i <= 10:
        print(i)
        i += 2

# 7 Funkce
def sum_and_multiply(a, b):
        return f"({a}+{b}) is "+str(a+b)

func = sum_and_multiply(2, 3)
print(func)
