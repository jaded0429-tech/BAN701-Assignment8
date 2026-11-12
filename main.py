import math

# Simple Number Calculator
# Welcome to this program that collects numbers and calculates their total and average.

def calculate_average(numbers):
    return sum(numbers) / len(numbers)


print("<3 SIMPLE NUMBER CALCULATOR <3")

while True:
    try:
        count = int(input("How many numbers would you like to enter?"))
        if count > 0:
            break
        print("Please enter a number greater than zero.")
    except ValueError:
        print("Sorry gorgeous. Please enter a whole number.")

numbers = []

for i in range(count):
    while True:
        try:
            number = float(input("Enter number: "))

            if math.isfinite(number):
                numbers.append(number)
                break
            else:
                print("Please enter a valid finite number.")
        except ValueError:
            print("Sorry gorgeous. Please enter a valid number.")

total = sum(numbers)
average = calculate_average(numbers)

print("\n<3 RESULTS <3")
print("Numbers entered:", numbers)
print("Total:", total)
print("Average:", average)

print("\nThank you for using the calculator!")