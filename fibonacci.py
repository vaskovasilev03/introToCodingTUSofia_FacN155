n = int(input("Enter an integer >> ")) + 2

n1, n2 = 0, 1

count = 0

if n <= 0:
    print("Invalid input!")
else:
    print(f"Fibonacci sequence upto {n-2} after 0 & 1:")
    while count < n:
        print(n1, end=" ")
        next = n1 + n2
        n1 = n2
        n2 = next
        count +=1