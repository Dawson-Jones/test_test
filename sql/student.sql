-- 数据的准备
    -- 创建一个数据库
    CREATE DATABASE python_text charset=utf8;
    -- 使用一个数据库
    USE python_text;
    -- 显示当前使用的数据库
    SELECT DATABASE();
    -- 创建一个数据表

-- 查询
    -- 查询所有字段
    SELECT * from students;
    SELECT * from classes;

    -- 查询指定字段
    SELECT name, age FROM students;

    -- 使用as起别名
    SELECT name AS 姓名, age AS 年龄 FROM students;
    -- select 表名.字段
    select s.name, s.age from students AS s;
    -- 去重
    SELECT DISTINCT gender from students;


-- 条件查询
    -- 比较运算符
    -- SELECT ... FROM 表名 WHERE ...
    
        -- 查询大于18岁的信息
        SELECT * FROM students WHERE age>18;
        -- 小于18
        SELECT id, name, gender FROM students WHERE age<18;
        -- 等于18 = 不是==
        select id, name, age FROM students WHERE age=18;
    
    -- 逻辑运算符
    -- and
        SELECT * from students WHERE age>18 and age<28;
        -- 18岁以上的女性
        select * from students WHERE age>18 and gender="女";
        select * from students WHERE age>18 and gender=2;

    -- or
        -- 18岁以上或者身高超过180的
        SELECT * from students WHERE age>18 or height>=180;

    -- not
        -- 不在 18岁以上的女性 这个范围的信息
        select * FROM students WHERE not (age>18 and gender=2);
        -- 年龄不是小于或者等于18 并且是女性
        SELECT * FROM students WHERE not age<=18 and gender=2;
        SELECT * FROM students WHERE (not age<=18) and gender=2;


-- 模糊查询
    -- like
    -- % 任意个 _替换一个
        -- 查询姓名中以"小"开头的名字
        SELECT name FROM students WHERE name like "小%";
        -- 查询姓名中,有"小"的名字
        SELECT name FROM students WHERE name like "%小%";
        -- 查询2个字的姓名
        SELECT * FROM students WHERE NAME like "__";
        -- 查询至少有2个字的名字
        SELECT * FROM students WHERE NAME like "__%";

    -- rlike 正则
        -- 查询以"周"开头的名字
        SELECT name FROM students WHERE name rlike "^周.*";
        -- 以"周"开头, 以'伦"结尾
        select * FROM students WHERE NAME rlike "^周.*伦$";


-- 范围查询
    -- BETWEEN AND
        -- 查询年龄为18 34 的姓名
        SELECT name, age FROM students WHERE age=18 or age=34;
        SELECT name, age FROM students WHERE age in (18,34);
        -- 年龄不是18 34 的姓名
        SELECT name, age FROM students WHERE age not in (18,34);

        -- 查询年龄在18~34之间的信息
        SELECT * FROM students WHERE age BETWEEN 18 and 34;
        -- 查询年龄不在18~34之间的信息
        SELECT * FROM students WHERE age not BETWEEN 18 and 34;
        -- SELECT * FROM students WHERE age not (BETWEEN 18 and 34);这个失败

-- 空判断
    -- is NULL
        -- 身高为空
        SELECT * FROM students WHERE height is NULL;
        -- 身高不为空
        SELECT * FROM students WHERE height is NOT NULL;


-- 排序
    -- ORDER BY 字段
    -- ASC 从小到大排列, 即升序
    -- DESC 从大到小排序, 即降序

        -- 查询年龄在18~34之间的男性, 按照年龄从小到大排序
        SELECT * FROM students WHERE (age BETWEEN 18 and 34) and gender=1 ORDER BY age;
        SELECT * FROM students WHERE (age BETWEEN 18 and 34) and gender=1 ORDER BY age ASC;
        -- 查询年龄在18~34之间的男性, 按照年龄从大到小排序
        SELECT * FROM students WHERE (age BETWEEN 18 and 34) and gender=1 ORDER BY age DESC;
        -- 查询年龄在18~34之间的女性, 按身高从高到矮排序
        SELECT * FROM students WHERE (age BETWEEN 18 and 34) AND gender=2 ORDER BY height DESC;
    
    -- ORDER BY 多个字段
        -- 查询年龄在18~34之间的女性, 按身高从高到矮排序,如果身高相同按照年龄从小到大排
        SELECT * FROM students WHERE (age BETWEEN 18 and 34) AND gender=2 ORDER BY height DESC, age ASC, id DESC;
        -- 按照年龄从小到大 身高从高到矮排序
        SELECT * FROM students ORDER BY age ASC, height DESC;


-- 聚合函数

    -- 总数
    -- count
        -- 查询男性有多少人, 女性有多少人
        SELECT count(*) FROM students WHERE gender=1;
        SELECT count(*) AS 男性总数 FROM students WHERE gender=1;
        SELECT count(*) AS 男性总数 FROM students WHERE gender=2;

    -- 最大值
    -- max
        -- 查询最大的年龄
        SELECT max(age) FROM students;
        -- 查询女性的最高身高
        SELECT max(height) FROM students WHERE gender=2;

    -- 最小值
    -- min
        -- 查询男性的最矮身高
        SELECT min(height) FROM students WHERE gender=1;

    -- 求和
    -- sum
        -- 计算所有人的年龄总和
        SELECT sum(age) FROM students;
        -- 计算平均年龄
        SELECT sum(age)/count(id) FROM students;
        SELECT sum(age)/count(*) FROM students;

    -- 平均值
    -- avg
        -- 计算平均年龄
        SELECT avg(age) FROM students;

    -- 四舍五入
    -- round(123.23, 1)保留以为小数
        -- 计算所有人的平均年龄， 保留2位小数
        SELECT round(avg(age), 2) FROM students;
        -- 计算男性平均身高， 保留两位小数
        select round(avg(height), 2) FROM students WHERE gender=1;


-- 分组
    -- GROUP BY
        -- 按照性别分组， 查询所有的性别
        SELECT gender, count(*) FROM students GROUP BY gender;
        -- 按性别分组， 计算最大身高
        SELECT gender, max(height) FROM students GROUP BY gender;
        -- 分组计算平均身高
        SELECT gender, avg(height) FROM students GROUP BY gender;
        -- 按性别分组， 并查看名字
        SELECT gender, GROUP_concat(name) FROM students GROUP BY gender;
        -- 计算男性人数
        SELECT count(*) FROM students WHERE gender=1;
        SELECT gender, count(*) FROM students where gender=1 GROUP BY gender;
        -- 查看男性分组中的人的名称， 年龄和id
        SELECT gender, GROUP_concat(name, " 年龄:", age, " id:", id) FROM students where gender=1 GROUP BY gender;

    -- HAVING 过滤
        -- 查询平均年龄超过30的性别, 并显示姓名
        SELECT gender, group_concat(name) FROM students GROUP BY gender HAVING avg(age)>30;
        SELECT gender, GROUP_concat(name), avg(age) FROM students GROUP BY gender HAVING avg(age)>30;
        -- 查询每种性别中人数多于两个的信息
        SELECT gender, GROUP_concat(name) FROM students GROUP BY gender HAVING count(id)>2;
        SELECT gender, GROUP_concat(name), count(id) FROM students GROUP BY gender;
    

-- 分页
    -- limit start, count
        
        -- 限制查询出来的数据个数
        SELECT * FROM students WHERE gender=1 limit 2;        
        -- 查询前五个数据
        SELECT * FROM student limit 0, 5;
        -- 查询6-10个数据
        SELECT * FROM students limit 5, 5; -- ------->limit (第N页-1)*每页的个数, 每页的个数
        -- 每页显示2个, 显示第6页的信息, 按照年龄从小到大排序
        SELECT * FROM students ORDER BY age ASC limit 10, 2;
        /*
        不可以是
        SELECT * FROM students limit 10, 2 ORDER BY age ASC;
        一定要limit放在最后
        */
        查询所有的女性信息并且按照身高从高到矮排序, 只显示2个
        SELECT * from students where gender=2 ORDER BY height DESC limit 2;

-- 连接查询
    -- INNER JOIN ... ON
        -- 查询有对应班级的学生以及班级信息
        SELECT * FROM students INNER JOIN classes on students.cls_id=classes.id;
        -- 按照要求显示姓名 班级
        SELECT students.name as 姓名, classes.name as 班级 FROM students INNER JOIN classes ON students.cls_id=classes.id;
        -- 班级显示在第一列, 并排序
        SELECT classes.name, students.* FROM students INNER JOIN classes ON students.cls_id=classes.id ORDER BY classes.name ASC, students.id ASC;
    
    -- LEFT JOIN
        -- 查询每位学生对应的班级信息
        SELECT * FROM students LEFT JOIN classes ON students.cls_id=classes.id;
        -- 查询没有班级的学生
        SELECT * FROM students LEFT JOIN classes ON students.cls_id=classes.id HAVING classes.id is NULL;
        SELECT * FROM students LEFT JOIN classes ON students.cls_id=classes.id WHERE classes.id is NULL;
       

-- 自关联
    -- 创建areas表
    CREATE TABLE areas(
        aid int PRIMARY KEY,
        atitile varchar(20),
        pid int
    );

