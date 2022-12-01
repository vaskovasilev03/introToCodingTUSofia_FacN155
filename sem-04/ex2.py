def list_avg(lst, multiplier = 1):
    sum, average, count = 0, None, 0

    if float(multiplier).is_integer():
        for i in lst:
            try:
                i = float(i)
                sum += i*multiplier
                count += 1
            except ValueError:
                continue
            except TypeError:
                continue
        if count != 0:
            average = sum / count
        else:
            print("Error: Divison by zero")
        return "Average of list is: " + str(average)
    else:
        print("Multiplier is not an integer")

print(list_avg(['4', 1.5, "@7$", 3.5, (1, "hi")]))
# print(list_avg(['6', 3, 3.0], 2))
# print(list_avg(['%$', {}]))
# print(list_avg([],2.5))
