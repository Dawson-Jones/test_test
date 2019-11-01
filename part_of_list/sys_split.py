import sys
import os

print(sys.argv[0])

name = 'jdq'
# os.path.split 把目录和文件分开
print(os.path.split(sys.argv[0]))

if not os.path.exists(name):
    os.makedirs(name)
