list = [12, 4, 1, 5, 67, 23, 54]
sort = []

while len(list)>0:
    min = list[0]
    for i in range(0, len(list)):
        if min > list[i]:
            min = list[i]

    sort.append(min)
    list.remove(min)

print(list)
print(sort)