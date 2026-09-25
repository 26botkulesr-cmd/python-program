n = int(input("Enter N: "))

count = 0
for i in range(1, n + 1):
    if i % 3 == 0:
        count += 1

print(f"Total numbers divisible by 3 from 1 to {n}: {count}")

