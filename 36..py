n = int(input("Enter N: "))

smallest = 1 if n >= 1 else n

print(f"The smallest number from 1 to {n} is: {smallest}")

min_num = 1
for i in range(1, n + 1):
    if i < min_num:
        min_num = i

print(f"Smallest using loop: {min_num}")
