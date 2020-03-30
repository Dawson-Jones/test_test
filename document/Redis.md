# Reids

### 键命令

| 含义                | 命令               | 示例                             |
| ------------------- | ------------------ | -------------------------------- |
| 查看所有键          | keys *             |                                  |
| 查看名称中含 a 的键 |                    | keys "a*"       加不加引号都可以 |
| 判断键是否存在      | exists key         | exists dawson                    |
| 查看键的 value 类型 | type key           | type dawson                      |
| 删除键及对应的值    | del key1 key2...   | del dawson yxt                   |
| 设置过期时间        | expire key seconds | expire dawson 10                 |
| 查看有效时间        | ttl key            | ttl dawson                       |



### string

| 含义               | 命令                             | 示例                                                      |
| ------------------ | -------------------------------- | --------------------------------------------------------- |
| 增                 | set key value                    | set dawson male                                           |
| 增 + 过期时间      | setex key seconds value          | setex dawson 10 male                                      |
| 增加多个值         | mset key1 value1 key2 value2 ... | mset l1 C l2 go l3 python l4 lua                          |
| 追加(好像并没有用) | append key value                 | append l1 language             # l1 从 C 变成了 Clanguage |
|                    |                                  |                                                           |
| 查                 | get key                          | get dawson                                                |
| 多查               | mget key1 key2...                | mget l1 l2 l3                                             |

### hash

> 键: {属性1: 值1, 属性2: 值2}
>
> > 值的类型为 string

| 含义                             | 命令                                      | 示例                         |
| -------------------------------- | ----------------------------------------- | ---------------------------- |
| 增                               | hset key field value                      | hset dawson sex male         |
| 多个键值                         | hmset key field1 value1 field2 value2 ... | hmset dawson sex male age 23 |
| 获取一个属性的值                 | hget key field                            | hget dawson sex              |
| 获取多个属性的值                 | hmget key field1 field2                   | hmget dawson sex age         |
| 获取指定键的所有属性             | hkeys key                                 | hkeys dawson                 |
| 获取所有属性的值                 | hvals key                                 | hvals dawson                 |
| 删除 hash 键                     |                                           | 见[键命令](#键命令)          |
| 删除属性, 属性对应的值会一起删除 | hdel key field1 field2...                 | hdel dawson sex              |

### list

> 列表的元素为 sring

| 含义                           | 命令                                  | 示例                  | 备注                                        |
| ------------------------------ | ------------------------------------- | --------------------- | ------------------------------------------- |
| 左侧插入                       | lpush key value1 value2 ...           | lpush a1 a b c        | c, b, a                                     |
| 右侧插入                       | rpush key value1 value2 ...           | rpush a1 0 1          | c, b, a , 0, 1                              |
| 在指定元素的前或者后插入新元素 | linsert key before element newelement | linsert a1 before b 3 | c, 3, b, a , 0, 1                           |
|                                |                                       |                       |                                             |
| 查询 a1 中所有元素             | lrange key start stop                 | lrange a1 0 -1        | 负数索引代表从尾部计数, -1 表示最后一个元素 |
| 修改指定索引的元素             | lset key index value                  | lset a1 1 z           | c, z, b, a , 0, 1                           |
| 删除指定元素                   | lrem key count value                  | lpush a2 a b a b a b  | count > 0 从头往尾移除                      |
|                                |                                       | lrem a2 -2 b          | count < 0 从尾往头移除                      |
|                                |                                       | lrange a2 0 -1        | count > 0 移除所有                          |

### set

> 无须
>
> 元素为 string
>
> 唯一, 不重复
>
> 无修改操作

| 含义               | 命令                        | 示例                |
| ------------------ | --------------------------- | ------------------- |
| 增加               | sadd key member1 member2... | sadd a3 sam sid kat |
| 获取key 中所有元素 | smembers key                | smembers a3         |
| 删除定制元素       | srem key member1 member2... | srem a3 sam         |

### zset

> sorted set
>
> 元素类型为 string
>
> 唯一, 不重复
>
> 每个元素关联一个 double 类型的 score 表示权重,通过全虫将元素从小到大排序
>
> 无修改操作
>
> > 感觉有点像优先队列的样子

| 含义                                 | 命令                                  | 示例                                         | 备注        |
| ------------------------------------ | ------------------------------------- | -------------------------------------------- | ----------- |
| 增加                                 | zadd key srore member1 srore2 member2 | zadd a4 4 lisi 5 wangwu 6 zhaoliu 3 zhangsan |             |
| 获取                                 | zrange key start stop                 | orange a4 0 -1                               | 遍历所有    |
| 获取score 值在 min 和 max 之间的元素 | zrangebyscore key min max             | zrangebyscore a4 5 6                         | 包含 5 和 6 |
| 获取元素的 score 值                  | zscore key member                     | zscore a4 zhangsan                           |             |
|                                      |                                       |                                              |             |
| 删除指定元素                         | zrem key member1 member2...           | zrem a4 zhangsan                             |             |
| 删除权重在指定范围的元素             | zremrangebuscore key min max          | zremrangebyscore a4 5 6                      |             |

