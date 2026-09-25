n = int(input("Enter N: "))

even_sum = 0
for i in range(2, n + 1, 2):
    even_sum += i

print(f"Sum of even numbers from 1 to {n}: {even_sum}")

