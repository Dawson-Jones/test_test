local ffi = require "ffi"

local myffi = ffi.load("add")

ffi.cdef[[
int add(int x, int y);
]]

local res = myffi.add(1,2)
print(res)
