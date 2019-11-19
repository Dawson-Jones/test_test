from xml.dom import minidom

# 加载xml文件到内存中
doc = minidom.parse('./xml/test_xml.xml')
# 获取根节点信息
xUsers = doc.getElementsByTagName('users')
# 打印的结果是只有一个数据的列表   xUsers = [<DOM Element: users at 0x2aee940>]
print('xUsers =', xUsers)
# 判断文件中是否存在users节点
if xUsers and len(xUsers) > 0:
    # 根据tag名，从users中获取所有的tag=user的节点列表
    # 从xUsers的打印信息可以看出，通过getElementsByTagName获取到的数据都是列表，所以需要使用xUsers[0]
    xUserList = xUsers[0].getElementsByTagName('user')
    # 打印结果: xUserList = [<DOM Element: user at 0x2aeef80>, <DOM Element: user at 0x2dde1c0>]
    # users下有多个user节点
    print('xUserList =', xUserList)
    # 循环遍历
    for user in xUserList:
        # id是包含在tag信息中的属性<user id='1'>，所以使用attributes获取
        id = user.attributes['id'].value
        # 打印结果: id = 1
        print('id =', id)
        # xUsername是一个列表
        xUsername = user.getElementsByTagName('username')
        if xUsername and len(xUsername) > 0:
            # 获取列表中的第一个数据
            # <username>admin</username>
            # 数据是包含在tag中的内容，所以使用firstChild.data获取
            username = xUsername[0].firstChild.data
            # username = admin
            print('username =', username)

        xEmail = user.getElementsByTagName('email')
        if xEmail and len(xEmail) > 0:
            email = xEmail[0].firstChild.data
            print('email =', email)

        xAge = user.getElementsByTagName('age')
        if xAge and len(xAge) > 0:
            age = xAge[0].firstChild.data
            print('age =', age)

        # <address><tag>xx通讯公司</tag></address>
        # xAddress是一个列表
        xAddress = user.getElementsByTagName('address')
        if xAddress and len(xAddress) > 0:
            # xAddress[0]是address这个tag
            # 从address这个标签中通过getElementsByTagName获取的数据也是列表
            xTag = xAddress[0].getElementsByTagName('tag')
            if xTag and len(xTag) > 0:
                # 不再包含子标签，直接通过firstChild.data获取数据
                tag = xTag[0].firstChild.data
                print(tag)
