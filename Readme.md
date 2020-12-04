## 本地运行步骤

1. `pip` 安装需要的第三方库

```
pip install -r requirement.txt
```

2. 修改`myNFCProject/settings` 配置文件

![image-20201204134220871](/images/image-20201204134220871.png)

3. 本地`mysql`数据库中创建NFCdb databases

![image-20201204134423908](/images/image-20201204134423908.png)

4. 生成迁移文件

```shell
# 切换到本项目所在的根目录下
cd myNFCProject 
# 执行如下命令， warehouse/migrations目录下生成新文件
python manage.py makemigrations
```

5. 进行迁移(所谓迁移就是像数据库中写入models.py中所定义的数据结构)

```shell
python manage.py migrate
```

6. 创建superuser

```shell
python manage.py createsuperuser
```

接着，创建username和password， 如下图所示

![image-20201204134956600](/images/image-20201204134956600.png)

7. 运行服务

```shell
python manage.py runserver
```

8. 浏览器输入http://localhost:8000/admin
9. 进入登录页面，输入刚刚创建的用户名和密码即可登录
10. 登录成功即可看到如下页面

![image-20201204135327821](/images/image-20201204135327821.png)

11. 进入Customer进行数据插入， 如下图所示

![image-20201204135644884](/images/image-20201204135644884.png)

点击图中红框位置，可以添加客户，具体如下图所示

![image-20201204135815374](/images/image-20201204135815374.png)





## 目前的数据表关系图

![image-20201204145537016](/images/image-20201204145537016.png)

这是现在的情况，后续还需要更新

