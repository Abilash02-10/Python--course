# ==========================================
# PYTHON OPERATORS AND INPUT/OUTPUT
# ==========================================

# ------------------------------------------
# 1. Arithmetic Operators
# ------------------------------------------

a = 10
b = 3

print("Arithmetic Operators")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)

print()


# ------------------------------------------
# 2. Comparison Operators
# ------------------------------------------

x = 10
y = 5

print("Comparison Operators")
print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= 10:", x >= 10)
print("y <= 5:", y <= 5)

print()


# ------------------------------------------
# 3. Assignment Operators
# ------------------------------------------

x = 10

x += 10
x *= 2
x -= 10

print("Assignment Operators")
print("Final value of x:", x)

print()


# ------------------------------------------
# 4. Logical Operators
# ------------------------------------------

x = 10
y = 20

print("Logical Operators")
print("x > 5 and y < 30:", x > 5 and y < 30)
print("x > 15 or y < 30:", x > 15 or y < 30)
print("not (x > 5):", not (x > 5))

print()


# ------------------------------------------
# 5. Membership Operators
# ------------------------------------------

fruits = ["apple", "banana", "cherry"]

print("Membership Operators")
print('"apple" in fruits:', "apple" in fruits)
print('"grape" not in fruits:', "grape" not in fruits)

print()


# ------------------------------------------
# 6. Identity Operators
# ------------------------------------------

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("Identity Operators")
print("a is b:", a is b)
print("a is c:", a is c)
print("a is not c:", a is not c)

print()


# ------------------------------------------
# 7. Bitwise Operators
# ------------------------------------------

x = 5
y = 3

print("Bitwise Operators")
print("x & y =", x & y)
print("x | y =", x | y)
print("x ^ y =", x ^ y)
print("~x =", ~x)
print("x << 1 =", x << 1)
print("9 << 2 =", 9 << 2)
print("9 >> 2 =", 9 >> 2)

print()


# ------------------------------------------
# 8. Input Formatting
# ------------------------------------------

print("Input Formatting")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
price = float(input("Enter price: "))

print("Name:", name)
print("Age:", age)
print("Price:", price)

print()


# ------------------------------------------
# 9. Output Formatting
# ------------------------------------------

print("Output Formatting")

name = "Alice"
age = 25

print("Name:", name, "Age:", age)

print("2026", "07", "15", sep="-")

print("hello", end="")
print("world")

print()


# ------------------------------------------
# 10. Formatted Output using f-string
# ------------------------------------------

name = "Charlie"
age = 28
score = 92.389

print(f"Name: {name} | Age: {age} | Score: {score:.2f}")
