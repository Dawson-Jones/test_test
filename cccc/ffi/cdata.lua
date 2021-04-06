local ffi = require("ffi")

ffi.cdef[[
    typedef struct {
        double x;
        double y;
    } vector_t;
]]


local vector

local mt = {
    __add = function(a, b)
        return vector(a.x + b.x, a.y + b.y)
    end,

    __len = function(a)
        return math.sqrt(a.x * a.x + a.y * a.y)
    end,

    __index = {
        area = function (a)
            return a.x * a.x + a.y * a.y
        end
    }
}

-- 声明 point 是 cdata
vector = ffi.metatype("vector_t", mt)

local a = vector(3, 4)
print(a.x, a.y)
print(#a)
print(a:area())

local b = a + vector(0.5, 8)
print(#b)