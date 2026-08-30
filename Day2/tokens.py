length = 10
width = 5
area = length * width

if area > 30:
    print("large area")
else:
    print("small area")

# Keywords
import keyword
print(keyword.kwlist)

# Multiple assignment
a, b, c = 10, 20, 30
print(a, b, c)

# Delete a variable
x = 100
del x

# This would cause an error because x was deleted:
# print(x)
