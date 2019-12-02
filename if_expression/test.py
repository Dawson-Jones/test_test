a, b, c = 1, 2, 3

# c = [b, a][a > b]

c = (a > b and [a] or [b])[0]

print(c)
