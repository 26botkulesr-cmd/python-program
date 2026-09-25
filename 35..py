n = int(input("Enter N: "))

largest = n

print(f"The largest number from 1 to {n} is: {largest}")

max_num = 1
for i in range(1, n + 1):
    if i > max_num:
        max_num = i

print(f"Largest using loop: {max_num}")
