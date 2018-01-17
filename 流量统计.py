#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author  : Soner
@version :
@Time    : 2017/11/3/0003 15:11
@license : Copyright(C), Your Company

获取包名方法：
1. adb logcat -c 清理
2. adb logcat | findstr START 获取
3. 启动相应的APP 进行获取包名
'''
__author__ = '$USER'
import os
import re
import time
import subprocess

def _exec(cmd):
    proc = subprocess.Popen(cmd)
    proc.wait()

def initADB():
    '''
    :启动adb
    '''
    cmd = 'adb start-server'
    _exec(cmd)


def initAPP(packagename):
    cmd = 'adb shell pm clear %s' % packagename
    _exec(cmd)


def startAPP(luanchActivity):
    cmd = 'adb shell am start %s' % luanchActivity
    _exec(cmd)


def getUserId(packagename):
    '''
    # 获取应用的uid
    '''
    cmd = 'adb shell dumpsys package %s | findstr userId' % packagename
    std = os.popen(cmd).readline()
    return std.split('=')[1].strip()


def getFlowFromUid(packagename, uid=None):
    '''
    # 通过应用uid，获取应用当前消耗的流量
    # return (rcv,snd)
    '''
    if uid is None:
        uid = getUserId(packagename)
    cmd = 'adb shell cat /proc/net/xt_qtaguid/stats | findstr %s' % uid
    std = os.popen(cmd)
    d_flow = []
    u_flow = []
    for line in std:
        if 'wlan' in line and '0x0' not in line:
            data = line.split()
            d_flow.append(int(data[5]))
            u_flow.append(int(data[7]))
    return sum(d_flow), sum(u_flow)


def getFlow(packagename, uid=None):
    if not uid:
        uid = getUserId(packagename)
    cmd_rcv = 'adb shell cat /proc/uid_stat/%s/tcp_rcv' % uid
    cmd_snd = 'adb shell cat /proc/uid_stat/%s/tcp_snd' % uid
    rcv = os.popen(cmd_rcv).readlines()[0].strip()
    snd = os.popen(cmd_snd).readlines()[0].strip()
    return eval(rcv), eval(snd)


# nowstrf = lambda: time.strftime("%Y%m%d%H%M%S", time.localtime())
# nowstamp = lambda: time.time()



if __name__ == '__main__':
    # 应用信息
    packagename = 'cn.com.haoluo.www'   # 待监测APP的包名
    luanchActivity = packagename + '/' + '.ui.LauncherActivity' #待监测APP的Activity

    # 监控20秒，监控多久自己控制
    LIMIT = 200

    # 初始化adb
    initADB()
    # 清除应用数据
    initAPP(packagename)

    # pid = getPID(packagename)
    uid = getUserId(packagename)

    # 获取应用初始上下行流量
    stard_rx, start_tx = getFlowFromUid(packagename, uid)

    # 启动应用
    startAPP(luanchActivity)

    # 开始监控
    n = 0
    while True:
        try:
            n += 1
            time.sleep(1)
            end_rx, end_tx = getFlowFromUid(packagename, uid)
            flow_rx, flow_tx = end_rx - stard_rx, end_tx - start_tx
            rx_kb, tx_kb = round(flow_rx / 1024, 3), round(flow_tx / 1024, 3)
            rx_mb, tx_mb = round(flow_rx / 1024 / 1024, 3), round(flow_tx / 1024 / 1024, 3)
            print(n,
                  '下行：', rx_kb, 'KB\t',
                  '上行：', tx_kb, 'KB\t',
                  '总流量', round(rx_kb + tx_kb, 3), 'KB\t\t',
                  '下行：', rx_mb, 'MB\t',
                  '上行：', tx_mb, 'MB\t',
                  '总流量', round(rx_mb + tx_mb, 3), 'MB\t'
                  )
            if n == LIMIT:
                break
        except KeyboardInterrupt:
            break

    print(
        '统计时长：%d s' % LIMIT
    )
    print(
        '实际下行流量：', rx_mb, 'MB\t',
        '实际上行流量：', tx_mb, 'MB\t',
        '实际总流量', round(rx_mb + tx_mb, 3), 'MB\t'
    )
