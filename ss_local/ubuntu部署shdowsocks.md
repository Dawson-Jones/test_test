## shdowsocks端

### 安装shadowsocks

- `sudo apt-get install python-pip`
- `sudo pip install shadowsocks`
- `pip install shadowsocks`

### 启动ss客户端

`sslocal -s server_ip -p server_port -l 1080 -k password -t 600 -m aes-256-cfb`

> -s表示服务IP, -p指的是服务端的端口，-l是本地端口默认是1080, -k 是密码（要加""）, -t超时默认300,-m是加密方法默认aes-256-cfb
>
> 可以简单的写为：sslocal -s ip -p port -k "password" #用-s -p -k这三个参数就好，其他的默认将服务端的加密方法设为aes-256-cfb。

举例：

`sslocal -s 207.148.4.54 -p 443 -k "jeedq.cn"`

### sh脚本

`cd Desktop`

`vim dl.sh`

`sslocal -s 207.148.4.54 -p 443 -k "jeedq.cn"`

现在可以使用`sh dl.sh`直接启动了

- 守护进程启动

  `nohup sh dl.sh &`

### 加入开机运行

在/etc下编辑一个叫rc.local 的文件，需要root权限。

`sudo vim /etc/rc.local` 编辑，在最下面输入 `nohup bash /home/dl.sh>/home/d.txt &` 保存。

重启后去看下d.txt，是/home/dl.sh line 3 :sslocal:command not found,打开浏览器果然是无法连接代理服务器

经过一番搜索我们发现原来linux是找不到sslocal这条命令？需要添加路径，我们发现sslocal 和ssserver这两个命令是被存在 /usr/local/bin/下面的，其实不用去profile添加了，直接把这两个文件移动到/bin下（同样需要root权限，你可以在root终端下使用cp复制命令）

这个时候reboot试试看？没错，现在你不用操心代理的事情了，开机直接科学自由网络冲浪！奔跑吧～少年！

## 代理插件SwitchyOmega端

[https://github.com/FelisCatus/SwitchyOmega/releases/ ](https://github.com/FelisCatus/SwitchyOmega/releases/ ) 下载插件，然后浏览器地址打开chrome://extensions/，安装插件。

`PROFILES`>`proxy`中选择`SOCKS5`，`127.0.0.1`，`1080`

模式为auto switch 类似于pac模式

将图中 **规则列表规则** 前面的框打√，再将后面的情景模式设置为 proxy，意思是规则列表中的内容，我们使用 proxy 情景模式。然后规则列表设置中：

> 规则列表格式： AutoProxy
> 规则列表网址： https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt