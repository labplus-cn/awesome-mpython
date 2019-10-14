<img width="500" src="http://wiki.labplus.cn/images/8/8a/ZKB-Xie.png"/>

## 概述

贝壳物联是一个让你与智能设备沟通更方便的物联网云平台，你可以通过互联网以对话、遥控器等形式与你的智能设备聊天、发送指令，查看实时数据，跟实际需求设置报警条件，通过APP、邮件、短信、微博、微信等方式通知用户。

repo 提供掌控板或micropython连接贝壳物联平台功能,你可以设备与设备间的通讯、上传传感器数据、或者通过web端或微信发送指令给设备。也可以通过智能语音助手(天猫),控制设备。实现语音控制。

- mPython library GitHub：https://github.com/labplus-cn/mPython-lib
- mPython Library Documentation：https://mpython-lib.readthedocs.io

## 库的安装方法

可通过以下任一方法进行安装。
1. 将项目中的`bigiot.py` 
2. 在掌控板REPL界面中，使用upip安装，步骤如下：
    * 前置条件需要掌控板连接网络
    * 导入upip模块，执行`import upip`
    * 执行`upip.install('mPython-bigiot')

```python
>>> import upip
>>> upip.install('mPython-bigiot')
```


## 执照

所有代码均在MIT许可下发布。