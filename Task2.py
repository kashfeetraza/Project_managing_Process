numbers = []

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("Your list is:", numbers)

print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))