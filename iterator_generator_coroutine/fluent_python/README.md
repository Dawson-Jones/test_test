- `yield from` 其实就是 `yield` 的语法糖  
    > A Python generator is a form of coroutine, but has the limitation that it can only yield to its immediate caller. This means that a piece of code containing a yield cannot be factored out and put into a separate function in the same way as other code. Performing such a factoring causes the called function to itself become a generator, and it is necessary to explicitly iterate over this second generator and re-yield any values that it produces.
- 主程序通过 `yield from` 直接和 `yield` 打通而 `yield` 会立即返回给主程序 导致主程序不会阻塞, 可以进行事件循环? -> `yield from` 和 `await` 就是让出控制权给调用方  
- `yield` 生成器的返回值 作为 `yield from` 的值 -> 这样做的原因是 可以像调用普通函数一样调用一个生成器  
- 任何*类似*堵塞型的操作, 要使用`await`让出控制权
