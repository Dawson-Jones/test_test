> yield from 语法初衷是为了能够分离一段在yield中的代码   

# yield from
`RESULT = yield from EXPR`

### 等价于  

```python

_i = iter(EXPR)
try:
    _y = next(_i)
except StopIteration as _e:
    _r = _e.value
else:
    while 1:
        try:
            _s = yield _y
        except GeneratorExit as _e:
            try:
                _m = _i.close
            except AttributeError:
                pass
            else:
                _m()
            raise _e
        except BaseException as _e:
            _x = sys.exc_info()
            try:
                _m = _i.throw
            except AttributeError:
                raise _e
            else:
                try:
                    _y = _m(*_x)
                except StopIteration as _e:
                    _r = _e.value
                    break
        else:
            try:
                if _s is None:
                    _y = next(_i)
                else:
                    _y = _i.send(_s)
            except StopIteration as _e:
                _r = _e.value
                break
RESULT = _r
```
***
# async with
```python
async with EXPR as VAR:
    BLOCK
```
### 等价于
```python
mgr = (EXPR)
aexit = type(mgr).__aexit__
aenter = type(mgr).__aenter__

VAR = await aenter(mgr)
try:
    BLOCK
except:
    if not await aexit(mgr, *sys.exc_info()):
        raise
else:
    await aexit(mgr, None, None, None)
```
An asynchronous context manager is a context manager that is able to suspend execution in its enter and exit methods.  
意思就是能在比如`with open()`这里暂停交出控制权, 也能在退出`with`暂停  
***
# async for
```python
async for TARGET in ITER:
    BLOCK
else:
    BLOCK2
```
### 等价于
```python
iter = (ITER)
iter = type(iter).__aiter__(iter)
running = True
while running:
    try:
        TARGET = await type(iter).__anext__(iter)
    except StopAsyncIteration:
        running = False
    else:
        BLOCK
else:
    BLOCK2
```
意思就是使用`async for` 的时候会调用`__aiter__`方法, `__aiter__`方法的返回值是一个异步迭代器, 使用异步迭代器的`__anext__`方法能够迭代异步代码, 就是循环中的每一个元素都是可以通过异步生成 -> 元素都使用了`await`
> 注意!!! 
```python
for i in iter:
    await i
```
和
```python
async for i in iter:
    i
```
有本质区别  
上面的如果生成i的时候会堵塞依旧会堵塞, 而下面的是生成i的时候让出控制权等i生成之后再进行下面的代码  