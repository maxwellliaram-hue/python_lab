from utils import square, is_even, celsius_to_fahrenheit, greet


value = input("Enter a number: ")
number = float(value)

print(f"Square: {square(number)}")
print(f"Even: {is_even(number)}")
print(f"Fahrenheit: {celsius_to_fahrenheit(number)}")
print(greet("Student"))

