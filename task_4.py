def proximity_calculation(arr1, arr2):
    proximity = 0
    # подсчёт ведётся до тех пор пока каждые новые значения в массивах равны
    min_len = min(arr1[0], arr2[0])
    for i in range(min_len):
        if arr1[1][i] == arr2[1][i]:
            proximity += 1
        else:
            break
    
    return proximity

n = int(input())
# использую генератор списков и создаю список кортежей, где первый 
# элемент это длина вложенного массива, а второй сам массив
arrays = [(int(input()), list(map(int, input().split()))) for _ in range(n)]
total = 0
for i in range(n):
    for j in range(i+1, n):
        # подсчёт количества близостей массивов
        total += proximity_calculation(arrays[i], arrays[j])

print(total)