def input_nums(n):
    nlist = list()
    if type(n) == int:
        for i in range(n):
            i = input(f"Enter list element[{i+1}]: ")
            if i.isnumeric():
                i = int(i)
                nlist.append(i)
            else:
                continue
    return nlist
    
def sum_list(lst):
    sum = 0
    for i in range(len(lst)):
        try:
            curr = float(lst[i])
            sum += curr
        except ValueError:
            continue
    print(f'Sum = {sum}')
    return sum

def max_of_two(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if float(a) > float(b) or float(a) == float(b):
            return a
        else:
            return b
    elif isinstance(a, (int, float)):
        return a
    elif isinstance(b, (int, float)):
        return b
    else:
        return ""

# input_nums(9)
# sum_list([1, "a", 3.14, "5"])
# sum_list(["asd", "-"])

# max_of_two(2.5, 13)
# max_of_two("@#$", {})
print(max_of_two(sum_list(input_nums(4)), sum_list(input_nums(3))))

# print(round(max_of_two(sum_list([4, "AA@", 3.12, "1"]), "9.2"), 2))