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
    call("pip2 install --upgrade " + dist.project_name, shell=True)
