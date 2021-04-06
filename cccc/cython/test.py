import ctypes

adder = ctypes.CDLL("./dyadd.so")

res_int = adder.add_int(4, 5)

print(res_int)

add_float = adder.add_float
add_float.restype = ctypes.c_float
a = ctypes.c_float(5.5)
b = ctypes.c_float(4.5)

print(str(adder.add_float(a, b)))
