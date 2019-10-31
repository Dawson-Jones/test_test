print([x for x in range(50) if x % 2 != 0])

names = [
    ['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
    ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']
]

# temp = list()
# for lst in names:
#     for name in lst:
#         # if name.count('e') >= 2:
#         # temp.append(name if name.count('e') >= 2)
#
# print(temp)

a = [name for lst in names for name in lst if name.count('e') >= 2]
print(a)

list_show = [1, 2, 3, 4]

print([x + 10 for x in list_show])
print(list(map(lambda x: x + 10, list_show)))

print(map(lambda x, y: x * y, range(9), range(9)))

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print([x for row in matrix for x in row])
print(list(map(lambda x, y: x + y, [1, 2, 3, 4], [2, 3, 4, 5])))

# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if i != k and j != k and i != j:
#                 print(i, j, k)


