### 关于《Python自动化测试实战》

书中错误：
注：p 代表page，198代表书中第198页

------

p198

```Python
Dumps() 方法可将 JSON 格式数据序列化为 Python 的相关数据类型（如列表、元组、字典等）；loads() 方法是
把 Python 数据类型转换为 JSON 相应的数据类型。
```

修改为：

```Python
loads() 方法可将 JSON 格式数据序列化为 Python 的相关数据类型（如列表、元组、字典等）；Dumps()方法是
把 Python 数据类型转换为 JSON 相应的数据类型。
```

------

p209

原文中  新增 Createlog() 方法

修改为： 

```
新增 Makelog()方法
```

代码中   def Createlog()   

修改为：  

```
def  Makelog()
```

------

p243、p253、p259、p260、p261

代码中：

```python
'deviceName': 'http://127.0.0.1:4723/wd/hub'
```

修改为 :

```python
'deviceName': '127.0.0.1:62001'
```

'127.0.0.1:62001' 为夜神模拟器的设备名

