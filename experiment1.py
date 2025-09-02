# Program to read two numbers and display bitwise operations

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

# Perform all bitwise operations
and_result = a & b
or_result = a | b
xor_result = a ^ b
xor_result = a + b
print("hello")


# Display results
print("\n--- Bitwise Operations ---")
print(f"Bitwise AND (&): {a} & {b} = {and_result}")
print(f"Bitwise OR (|): {a} | {b} = {or_result}")
print(f"Bitwise XOR (^): {a} ^ {b} = {xor_result}")
print(f"Bitwise XOR (^): {a} * {b} = {xor_result}")
print(f"Bitwise XOR (^): {a} + {b} = {xor_result}")
