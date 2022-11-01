num = int(input('Please input an integer! '))
pos = int(input('Please input the bit you want to check... '))

print(bin(num))
if num & (1 << pos):
    print('1')
else:
    print('0')
