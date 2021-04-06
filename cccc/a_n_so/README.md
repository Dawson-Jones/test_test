# C 语言编译详解

## 使用静态库  

```
.
├── math_test.c
├── math_test.h
├── README.md
└── use_staticmath.cc
```

1. 编译目标文件 `.o`  
`gcc -c math_test.c -o staticmath.o`  
2. ar 目标文件, 生成打包后的 `.a` 静态库  
`ar -crv libstaticmath.a staticmath.o`  
3. 编写代码见 `use_staticmath.c`  
4. 编译  
`gcc use_staticmath.c -L . -l staticmath`  
    - `-L` 指定静态库搜索路径  
    - `-l` 指定静态库的名字, don't need prefix `lib` and suffix `.a` or `.so`  

编译之后的样子

```
a_n_so
├── a.out
├── libstaticmath.a
├── README.md
├── staticmath.c
├── staticmath.h
├── staticmath.o
└── use_staticmath.c
```

ldd 查看 `ldd ./a.out`  
```
linux-vdso.so.1 =>  (0x00007fffd99f3000)
libc.so.6 => /lib64/libc.so.6 (0x00007f327a4a6000)
/lib64/ld-linux-x86-64.so.2 (0x00007f327a881000)
```  

## 使用动态库

1. 生成目标文件  
`gcc -fPIC -c math_test.c -o dynmath.o`
2. 生成动态 `so` 库  
`gcc -shared -o libdynmath.so dynmath.o`

   > 1, 2 命令可以合在一起:  
   > `gcc -fPIC -shared -o libdynmath.so math_test.c`

3. 编译  
`gcc use_staticmath.c -L . -l dynmath`

> 注意: 编译完成后, 并不能运行, ldd 查看

```
$ ldd ./a.out 
linux-vdso.so.1 =>  (0x00007fff82558000)
libdynmath.so => not found
libc.so.6 => /lib64/libc.so.6 (0x00007f5de8c8d000)
/lib64/ld-linux-x86-64.so.2 (0x00007f5de9069000)
```

4. 执行的时候是如何定位共享库文件  
当系统加载可执行代码时候，能够知道其所依赖的库的名字，但是还需要知道绝对路径。此时就需要系统动态载入器(dynamic linker/loader)。  
对于elf格式的可执行程序，是由ld-linux.so*来完成的，它先后搜索elf文件的 DT_RPATH段—环境变量LD_LIBRARY_PATH—/etc/ld.so.cache文件列表—/lib/,/usr/lib 目录找到库文件后将其载入内存。  
    - 方法 1  
    `cp libdynmath.so /usr/lib64`
    - 方法 2  
    编辑/etc/ld.so.conf文件，加入库文件所在目录的路径  

比较静态库和动态库生成的 *.o* 文件  
```
$ stat dynmath.o
  File: dynmath.o
  Size: 1520            Blocks: 8          IO Block: 4096   regular file
Device: 803h/2051d      Inode: 68106872    Links: 1
Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2021-02-08 13:47:49.496291549 +0800
Modify: 2021-02-08 13:47:35.097292562 +0800
Change: 2021-02-08 13:47:35.097292562 +0800
 Birth: -
$ md5sum staticmath.o
424053f4ac3cf121529dcea67d7e1b19  staticmath.o


$ stat staticmath.o 
  File: staticmath.o
  Size: 1520            Blocks: 8          IO Block: 4096   regular file
Device: 803h/2051d      Inode: 68106862    Links: 1
Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2021-02-08 13:46:09.080298617 +0800
Modify: 2021-02-08 13:45:52.879299758 +0800
Change: 2021-02-08 13:45:52.879299758 +0800
 Birth: -

$ md5sum dynmath.o
424053f4ac3cf121529dcea67d7e1b19  dynmath.o
```

生成的文件好像并没有什么不同  

## 编译过程  

> 预处理 -> 编译 -> 汇编 -> 链接

1. 预处理  
展开代码（进行宏替换）
    - 预处理功能主要包括宏替换、替换头文件、条件编译、删除注释等。
    - 实例：`gcc -E 文件名 -o 文件名.i`
    - 选项’-E’ 作用是让gcc在预处理结束后停止编译。

2. 编译  
生成汇编代码  
    - 在这个阶段中，gcc首先要检查代码的规范性、是否有语法错误等，检查无误后，将代码翻译为汇编语言。  
    - 实例：`gcc -S 文件名.i -o 文件名.s`  

3. 汇编
将汇编代码编译称为机器可识别的指令  
    - 实例：`gcc -c 文件名.s -o 文件名.o`  
    > 前面三步只是将自身代码编译称为机器代码，但是在我们的代码中有许多调用函数，比如printf、malloc、等，这些函数都不是我们自己实现的，但是如果我们要生成最后的可执行程序，那么就必须在我们的代码中知道这些函数的实现。  
    最后的答案是：系统把这些函数实现做到名为libc.so.6的库文件中去了，在没有特别指定时，gcc会到系统默认的搜索路径“/usr/lib”下进行查找，也就是链接到libc.so.6库函数中去，这样就能实现函数了。  

4. 链接  
生成可执行文件或函数库
    - 实例：`gcc 文件名.o -o 文件名`

函数库一般分为静态库和动态库两种  
**静态库**：将库中的代码全部拿过来跟我们的代码一起写入最终的可执行程序，最终生成的可执行程序比较大，但运行时不需要依赖库文件。  
**动态库**：记录函数地址信息，并不是将代码全部拿过来，所以可执行程序比较短，但是需要依赖库文件。  
gcc默认动态链接！
