## fkfish

压榨不死, 摸鱼不停

本项可以伪装成重启或者蓝屏等界面，目的是使得广大的无产阶级兄弟们可以在资本家的无理压迫下合理的摸鱼, 比如以下情况:

1. 无意义的加班
2. 无工资的加班
3. 超时的加班
4. 其他违法的加班
5. 剥夺员工上厕所的权利
6. 剥夺员工休息的权力

不鼓励正常工作时间过多的摸鱼, 但是坚决反对压榨加班

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
fkfish  ## 根据不同系统，伪装成重启界面
```

- 退出
```
<ctrl + m>
```

- 更多功能
```python
fkfish -m winblue  ## 伪装windows蓝屏
```