n = int(input("Enter N: "))

print(f"Prime numbers from 1 to {n}:")

for i in range(2, n + 1):
    is_prime = True
    
   
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break  
s
    if is_prime:
        print(i)
