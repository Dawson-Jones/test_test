a, b, c = 1, 2, 3

c = [a, b][a > b]

# c = (a > b and [a] or [b])[0]
# c = a > b and a or b

print(c)
