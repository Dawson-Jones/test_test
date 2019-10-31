import time
import base64

ctime = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
print(ctime)

with open('/home/ubuntu/Pictures/test/t/1.txt', 'rb') as f:
    content = f.read()
    print(content)
    b64_content = base64.b64encode(content).decode()
    print(b64_content)


from copy import deepcopy

a = [1, 2]
b = [a, 3]
print(b)  # [[1,2],3]
a.append(b)
print(a)
