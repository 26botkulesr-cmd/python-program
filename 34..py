n = int(input("Enter N: "))

odd_sum = 0
for i in range(1, n + 1, 2):
    odd_sum += i

print(f"Sum of odd numbers from 1 to {n}: {odd_sum}")

