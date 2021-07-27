-- 1. 创建数据库
create database python4 charset=utf8;

-- 2. 删除数据库
drop database 数据库名;

-- 3. 查看当前所有的数据库
	show databases;

-- 4. 打开指定的库
	use 库名;

-- 5. 查看当前库的所有表
	show tables;

-- 6. 查看其他库的所有表
	show tables from 库名;

-- 7. 创建表
	create table 表名(
	列名 列类型,
	列名 列类型
	);
	CREATE TABLE xxxx(
		id int PRIMARY key not null auto_increment, 
		name varchar
		);

-- 8. 查看表结构
	desc 表名;

-- 9. 查看服务器版本
	-- 方式一: 登录到MySQL服务端
		select version();
	-- 方式二: 没有登录到MySQL
		mysql --version
		mysql -V

-- 10. 设置自增主键id的起始值
	-- 修改user表，主键自增从100开始
	alter table user AUTO_INCREMENT=10000;


-- mysql的语法规范
	-- 1. 不区分大小写, 但建议关键字大写, 表名/列名小写
	-- 2. 每条命令用分号结尾
	-- 3. 每条命令根据需要, 可以进行缩进或换行
	-- 4. 注释:
		单行注释: #注释文字
		单行注释: -- 注释文字
		多行注释: /* 注释文字 */
		
-- 显示时间
select now();


-- 实例
-- 1. 创建数据库, 编码utf-8, 名为mysqkpython
	CREATE DATABASE mysqlpython CHARSET=utf8;

-- 2. 使用数据库mysqlpython
	USE mysqlpython;

-- 创建表
	CREATE TABLE students(
		-- id, int类型, 无负数, 主键, 自动增长, 不能为空
		id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT NOT NULL,
		NAME VARCHAR(20) DEFAULT '',
		age TINYINT UNSIGNED DEFAULT 0,
		height DECIMAL(5,2),
		gender ENUM('男','女','中性','保密') DEFAULT '保密',
		cls_id INT UNSIGNED DEFAULT 0,
		is_delete BIT DEFAULT 0
	);
	CREATE TABLE students2 (
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT NOT NULL,
	NAME VARCHAR (20) DEFAULT ''
	) ;

-- 添加一列信息
	INSERT INTO students 
	VALUES
	(0, "贾冬青", 22, 187.50, "男", 0, 0);
	-- 或
	INSERT INTO students
	(id, name, age, height, gender, cls_id, is_delete)
	VALUES
	(0, "贾冬青"， 22， 187.50, "男", 0, 0);
 
 -- 查看表
	SELECT * FROM students;

INSERT INTO students VALUES
(0,'小明',18,180.00,2,1,0),
(0,'小月月',18,180.00,2,2,1);

-- 增加表字段
	ALTER TABLE students ADD birthday DATE;
-- 删除表 字段
	ALTER TABLE students DROP is_delete;

-- 查看表结构
	DESC students;

-- 修改表字段, 不重命名
	ALTER TABLE students MODIFY birthday DATETIME;
	ALTER TABLE students MODIFY birthday DATE;
-- 修改表字段, 重命名
	ALTER TABLE students CHANGE birthday birth DATE;

-- 删除
	DROP DATABASE 库名;
	DROP TABLE 表名;
	ALTER TABLE 表名 DROP 列名;

INSERT INTO students(NAME, gender) VALUES("小乔", 2);
INSERT INTO students(NAME, gender) VALUES("小乔", 2), ("貂蝉", 2);

SELECT * FROM students;

-- 修改表信息
	UPDATE students SET gender=1 WHERE id=8;
	UPDATE students SET age=21;
	UPDATE students SET birth=1996-01-15;
	UPDATE students SET age=22, gender=1 WHERE id=3;
	UPDATE students SET age=age+2 where id=1;

-- 查看指定信息
	SELECT * FROM students WHERE NAME="小乔";
	SELECT * FROM students WHERE id>6;

	SELECT NAME,gender FROM students WHERE id<6;
	SELECT NAME AS "姓名",gender AS "性别" FROM students;
	SELECT id AS 序号,gender AS "性别",NAME AS "姓名" FROM students;

-- 删除
	-- 物理删除
		DELETE FROM students; -- 全删慎用
		DELETE FROM students WHERE id=2;

	-- 逻辑删除
		ALTER TABLE students ADD is_delete BIT DEFAULT 0;
		SELECT * FROM students;
		UPDATE students SET is_delete=1 WHERE id=5;
