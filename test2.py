import sys
import os

print(sys.argv[0])

name = 'jdq'
print(os.path.split(sys.argv[0]))

if not os.path.exists(name):
    os.makedirs(name)