# ==========================================
# PYTHON INPUT FORMATTING
# ==========================================

# 1. Integer input
age = int(input("Enter your age: "))
print("Age:", age)
print("Type:", type(age))


# 2. Float input
height = float(input("Enter your height: "))
print("Height:", height)
print("Type:", type(height))


# 3. String input
name = input("Enter your name: ")
print("Name:", name)
print("Type:", type(name))


# 4. List input
numbers = list(map(int, input("Enter numbers: ").split()))
print("List:", numbers)
print("Type:", type(numbers))


# 5. Tuple input
numbers = tuple(map(int, input("Enter numbers: ").split()))
print("Tuple:", numbers)
print("Type:", type(numbers))


# 6. Set input
numbers = set(map(int, input("Enter numbers: ").split()))
print("Set:", numbers)
print("Type:", type(numbers))


# 7. Dictionary
# Example: key=value pairs
data = input("Enter name and age: ").split()

student = {
    "name": data[0],
    "age": int(data[1])
}

print("Dictionary:", student)
print("Type:", type(student))


# ==========================================
# MULTIPLE INPUTS
# ==========================================

# Two integer values
a, b = map(int, input("Enter two numbers: ").split())

print("a =", a)
print("b =", b)
print("Sum =", a + b)


# Three integer values
a, b, c = map(int, input("Enter three numbers: ").split())

print("a =", a)
print("b =", b)
print("c =", c)


# Name and marks
name, marks = input("Enter name and marks: ").split()

print("Name:", name)
print("Marks:", int(marks))


# Email and password
email, password = input("Enter email and password: ").split()

print("Email:", email)
print("Password:", password)


# ==========================================
# EVAL FUNCTION
# ==========================================

# eval() can convert input into its Python representation.

value = eval(input("Enter a value: "))

print("Value:", value)
print("Type:", type(value))


# Examples:
# Enter: 10       -> int
# Enter: 12.5     -> float
# Enter: "abhi"   -> str
# Enter: [1,2,3]  -> list
# Enter: (1,2,3)  -> tuple


# ==========================================
# STRING CONCEPTS
# ==========================================

s = "codegnana"

# Empty string
empty = ""

print("Empty string:", empty)

# String concatenation
print("Concatenation:", "codegnan" + "PFS")

# String repetition
print("Repetition:", "codegnana" * 3)

# Repeating a character
print("*" * 5)


# ==========================================
# STRING INDEXING
# ==========================================

s = "codegnana"

print("String:", s)

# Positive indexing
print("s[0] =", s[0])
print("s[4] =", s[4])

# Negative indexing
print("s[-1] =", s[-1])
print("s[-2] =", s[-2])


# ==========================================
# STRING SLICING
# ==========================================

names = "sajid abdul srinivas dherraj"

print("First name:", names[0:5])
print("First name:", names[:5])

print("abdul:", names[6:11])
print("srinivas:", names[12:20])
print("dherraj:", names[21:])

# Reverse last part
print("Reverse dherraj:", names[-1:-8:-1])


# ==========================================
# IN OPERATOR
# ==========================================

print("sajid" in names)
print("dherraj" in names)
print("karthik" in names)
