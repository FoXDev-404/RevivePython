# ============================================================
# VARIABLES - Basic Concepts
# ============================================================

# 1. BASIC VARIABLE ASSIGNMENT
# ============================================================
name = "John"
print(f"Hello There {name} How are you?")

# Get user input and check name length
user_name = input("Enter your name: ")
print(f"Length of your name: {len(user_name)}")


# 2. VARIABLE SWAP (using temporary variable)
# ============================================================
glass1 = "milk"
glass2 = "juice"
print(f"\nBefore swap: glass1 = {glass1}, glass2 = {glass2}")

temp = glass1
glass1 = glass2
glass2 = temp

print(f"After swap: glass1 = {glass1}, glass2 = {glass2}")


# 3. DATA TYPES
# ============================================================
print("\n--- Data Types ---")
age = 25  # integer
height = 5.9  # float
is_student = True  # boolean
name = "Alice"  # string

print(f"name: {name} -> type: {type(name)}")
print(f"age: {age} -> type: {type(age)}")
print(f"height: {height} -> type: {type(height)}")
print(f"is_student: {is_student} -> type: {type(is_student)}")


# 4. TYPE CONVERSION
# ============================================================
print("\n--- Type Conversion ---")
number = 123456
number_str = str(number)  # Convert integer to string
print(f"Original: {number} (type: {type(number)})")
print(f"Converted: {number_str} (type: {type(number_str)})")

# String concatenation with type conversion
result = int("123") + int("456")
print(f"int('123') + int('456') = {result}")

# Multiple type conversions
print(f"str(100): {str(100)}")
print(f"int('500'): {int('500')}")
print(f"float('3.14'): {float('3.14')}")
print(f"bool(1): {bool(1)}")


# 5. PRACTICAL EXAMPLE: Count letters in name
# ============================================================
print("\n--- Counting Letters ---")
user_name = input("Enter your name: ")
name_length = len(user_name)
message = "Number of letters in your name: " + str(name_length)
print(message)
