n = int(input("Enter an integer >> "))
nlist = []
for i in range(n):
    i = int(input())
    nlist.append(i)

print("Untouched list: " + str(nlist))
while True:
    cond = input("Choose condition: 1/0: ")
    if cond == "0":
        for i in range(len(nlist)):
            if i % 2 == 0:
                nlist[i] += 5
        print("Succesfully added +5 at even indexes")
        break
    elif cond == "1":
        for i in range(len(nlist)):
            if i % 2 != 0:
                nlist[i] += 10
        print("Succesfully added +10 at odd indexes")
        break
    else:
        print("Invalid condition! ->>> 1 OR 0")

print("Updated list: " + str(nlist))