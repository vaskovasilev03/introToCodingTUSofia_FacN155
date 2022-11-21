n = int(input("Enter an integer >> "))
count = 1
nlist = []
nsum = 0
while count <= n:
    curr = str(n) * count
    nlist.append((curr))
    nsum += int((curr))
    count += 1

print('+'.join(nlist) + " = ", end="")

print(nsum)