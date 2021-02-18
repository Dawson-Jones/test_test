# 使用静态库  

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

# 使用静态库
1. 生成目标文件  
`gcc -fPIC -c math_test.c -o dynmath.o`
> 生成的文件与 -c 生成的好像并没有什么不同, 下是文件的 md5 值  
```
$ stat dynmath.o
  File: dynmath.o’
  Size: 1520            Blocks: 8          IO Block: 4096   regular file
Device: 803h/2051d      Inode: 68106872    Links: 1
Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2021-02-08 13:47:49.496291549 +0800
Modify: 2021-02-08 13:47:35.097292562 +0800
Change: 2021-02-08 13:47:35.097292562 +0800
 Birth: -
$ stat ‘staticmath.o 
  File: ‘staticmath.o’
  Size: 1520            Blocks: 8          IO Block: 4096   regular file
Device: 803h/2051d      Inode: 68106862    Links: 1
Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2021-02-08 13:46:09.080298617 +0800
Modify: 2021-02-08 13:45:52.879299758 +0800
Change: 2021-02-08 13:45:52.879299758 +0800
 Birth: -

$ md5sum staticmath.o
424053f4ac3cf121529dcea67d7e1b19  staticmath.o
$ md5sum dynmath.o
424053f4ac3cf121529dcea67d7e1b19  dynmath.o

```
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