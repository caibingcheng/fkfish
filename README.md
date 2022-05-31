## fkfish

压榨不死, 摸鱼不停

本项可以伪装成重启或者蓝屏等界面，目的是使得广大的无产阶级兄弟们可以在资本家的无理压迫下合理的摸鱼, 比如以下情况:

1. 无意义的加班
2. 无工资的加班
3. 超时的加班
4. 其他违法的加班
5. 剥夺员工上厕所的权利
6. 剥夺员工休息的权力

合理的摸鱼可以提高工作和学习的效率，有益身心健康，不鼓励正常工作时间过多的摸鱼, 但是坚决反对压榨加班

### 使用

本项目依赖`Python`以及`tkinter`, 因此在你的系统上需要安装上述依赖

#### 环境

- Ubuntu

```Shell
apt install python3
apt install python3-tk
```

- Windows

`tkinter`是`Python`的内置特性, 因此在安装`Python`的时候勾选安装`tk`即可.

#### 安装

源码或`pip`安装, 推荐使用`pip`安装

- 源码安装

```python
git clone git@github.com:caibingcheng/fkfish.git
cd fkfish
python3 setup.py install
```

- pip安装

```python
pip3 install fkfish
```

#### 运行

- 运行

```python
## 自动根据不同系统，伪装成重启界面
fkfish
```

Linux:
!["Linux-Demo"](statics/fkfish_demo_0.gif) 

Windows:
!["Windows-Demo"](statics/fkfish_demo_1.gif)

- 退出
```python
## 如果设置了密码，则该热键不生效
<ctrl + m>
```

- windows 蓝屏
```python
## 伪装windows蓝屏
fkfish -m winblue
```

- 设置密码
```python
## <ctrl + m>失效，密码匹配后才可以退出
fkfish -p [passwd]
```


### TODO

- 屏蔽系统热键
  