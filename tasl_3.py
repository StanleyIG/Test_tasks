n, m, q = map(int, input().split())
columns = input().split()
# если надо задействовать переменную m
# columns = []
# for i in range(m):
#     if len(columns) == m:
#         break
#     columns += list(map(str, input().split()))
table = [list(map(int, input().split())) for _ in range(n)]
constraints = [input().split() for _ in range(q)]

total = 0
for row in table:
    is_true = True
    for column_name, symbol, val in constraints:
        col_index = columns.index(column_name)
        if symbol == '<':
            if not (row[col_index] < int(val)):
                is_true = False
                break
        elif symbol == '>':
            if not (row[col_index] > int(val)):
                is_true = False
                break

    if is_true:
        total += sum(row)
        
print(total)
