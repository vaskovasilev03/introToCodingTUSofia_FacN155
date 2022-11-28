n = int(input("Enter an integer >> "))
count, nfact = n, 1
while count > 0:
    nfact *= count
    count -= 1

print(f"Factorial of n(!{n}) --> {nfact}")