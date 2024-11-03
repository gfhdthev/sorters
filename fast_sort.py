unsorted_list = [2, 4, 632, 1, 4, 53, 126, 53, 86, 3, 321, 563, 9999]

# Создаем стек для хранения начала и конца каждого подмассива
stack = [(0, len(unsorted_list) - 1)]
    
while stack:
    start, end = stack.pop()
        
    # Если подмассив содержит один или ноль элементов, он уже отсортирован
    if start >= end:
        continue
        
    # Выбираем опорный элемент (например, последний элемент)
    pivot = unsorted_list[end]
    i = start - 1
        
    # Разделяем элементы по отношению к опорному элементу
    for j in range(start, end):
        if unsorted_list[j] < pivot:
            i += 1
            unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i]
        
    # Ставим опорный элемент на его правильную позицию
    i += 1
    unsorted_list[i], unsorted_list[end] = unsorted_list[end], unsorted_list[i]
        
    # Добавляем новые подмассивы в стек
    stack.append((start, i - 1))  # Левый подмассив
    stack.append((i + 1, end))    # Правый подмассив

print(unsorted_list)