# Simple Number Calculator
# Welcome to this program that collects numbers and calculates their total and average.

def calculate_average(numbers):
    return sum(numbers) / len(numbers)


print("<3 SIMPLE NUMBER CALCULATOR <3")

count = int(input("How many numbers would you like to enter?"))

numbers = []

for i in range(count):
    number = float(input("Enter number: "))
    numbers.append(number)

total = sum(numbers)
average = calculate_average(numbers)

print("\n<3 RESULTS <3")
print("Numbers entered:", numbers)
print("Total:", total)
print("Average:", average)

print("\nThank you for using the calculator!")