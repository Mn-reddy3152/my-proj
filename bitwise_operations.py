# Program to demonstrate bitwise operations on two numbers

def main():
    # Read two numbers from user
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    # Perform bitwise operations
    bitwise_and = num1 & num2
    bitwise_or = num1 | num2
    bitwise_xor = num1 ^ num2
    
    # Display results
    print("\n--- Bitwise Operations Results ---")
    print(f"Numbers: {num1} and {num2}")
    print(f"Binary representation:")
    print(f"  {num1} = {bin(num1)}")
    print(f"  {num2} = {bin(num2)}")
    print()
    print(f"Bitwise AND (&): {num1} & {num2} = {bitwise_and} ({bin(bitwise_and)})")
    print(f"Bitwise OR (|): {num1} | {num2} = {bitwise_or} ({bin(bitwise_or)})")
    print(f"Bitwise XOR (^): {num1} ^ {num2} = {bitwise_xor} ({bin(bitwise_xor)})")

if __name__ == "__main__":
    main()
