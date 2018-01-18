#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author  : Soner
@version : 
@Time    : 2017/11/3/0003 15:11
@license : Copyright(C), Your Company 
'''
import pip
from subprocess import call
from time import sleep

for dist in pip.get_installed_distributions():
    # 执行后，pip默认为Python3版本
    # 双版本下需要更新Python2版本的包，使用py2运行，并将pip修改成pip2
    call("pip install --upgrade " + dist.project_name, shell=True)
