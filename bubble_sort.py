list = [2, 6, 1, 3, 11, 111, 6, 7, 3, 65, 2, 67, 9]
stop_flag = True
while stop_flag is True:
    stop_flag = False
    for i in range(0, len(list)-1):
        if list[i] > list[i+1]:
            change = list[i]
            list[i] = list[i+1]
            list[i+1] = change
            stop_flag = True
print(list)