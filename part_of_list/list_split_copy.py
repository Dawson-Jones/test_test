li = list(range(100))

li1 = li[:]

print(li)

for i in li1:
    li.remove(i)

print(li)
print(li1)
