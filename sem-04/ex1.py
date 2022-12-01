def representsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

n = int(input("Input an integer >> "))

ndict = dict()
while n > 0:
    keyinput = input("Key >> ")
    valueinput = input("Value >> ")
    if representsInt(valueinput):
        ndict[keyinput] = int(valueinput)
    else:
        ndict[keyinput] = valueinput
    n -= 1

print(ndict)

m = int(input("Input an integer >> "))

mlist = list()

for i in range(m):
    i = input("Input value >> ")
    if i in ndict.keys():
        mlist.append(ndict[i])
        del ndict[i]
    else:
        mlist.append(i)


print(ndict)
print(mlist)