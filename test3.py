str3 = "ABCD \nabc \nis \nis is end"
print(str3.count("\n"))  # 就是从下标8以后开始
# (输出)	3

print(str3.count("is", 10, len(str3)))  # 就是从下标9以后开始
# (输出)	2
