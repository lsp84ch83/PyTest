#!/usr/bin/env python
# _*_ coding: utf-8 _*_
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
    net_rcv_bck = []
    net_rcv_front = []
    net_snd_bck = []
    net_snd_front = []

    lo_rcv_bck = []
    lo_rcv_front = []
    lo_snd_bck = []
    lo_snd_front = []

    for line in std:
        data = line.split()
        if 'ccmni0' in line:
            background_flow = int(data[4]) == 0
            if background_flow:
                net_rcv_bck.append(int(data[5]))
                net_snd_bck.append(int(data[7]))
            else:
                net_rcv_front.append(int(data[5]))
                net_snd_front.append(int(data[7]))
        elif 'lo' in line:
            background_flow = int(data[4]) == 0
            if background_flow:
                lo_rcv_bck.append(int(data[5]))
                lo_snd_bck.append(int(data[7]))
            else:
                lo_rcv_front.append(int(data[5]))
                lo_snd_front.append(int(data[7]))
    return sum(net_rcv_bck), sum(net_rcv_front), sum(net_snd_bck), sum(net_snd_front), \
            sum(lo_rcv_bck), sum(lo_rcv_front), sum(lo_snd_bck), sum(lo_snd_front)


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
    packagename = 'cn.hollo.mirror.service'   # 待监测APP的包名
    launchActivity = packagename + '/' + '.ui.LauncherActivity' #待监测APP的Activity

    # 监控20秒，监控多久自己控制
    LIMIT = 86400

    # 初始化adb
    initADB()
    # 清除应用数据
    #initAPP(packagename)

    # pid = getPID(packagename)
    uid = (getUserId(packagename))[0:5]
    #uid = uid1[0:5]
    print(uid)
    # 获取应用初始上下行流量
    net_bck_start_rx, net_front_start_rx, net_bck_start_tx, net_front_start_tx, \
        lo_bck_start_rx, lo_front_start_rx, lo_bck_start_tx, lo_front_start_tx = getFlowFromUid(packagename, uid)
    
    net_start_rx = net_bck_start_rx + net_front_start_rx
    net_start_tx = net_bck_start_tx + net_front_start_tx
    lo_start_rx = lo_bck_start_rx + lo_front_start_rx
    lo_start_tx = lo_bck_start_tx + lo_front_start_tx

    # 启动应用
    #startAPP(launchActivity)

    # 开始监控
    n = 0
    while True:
        try:
            n += 1
            time.sleep(1)
            net_bck_end_rx, net_front_end_rx, net_bck_end_tx, net_front_end_tx, \
            lo_bck_end_rx, lo_front_end_rx, lo_bck_end_tx, lo_front_end_tx = getFlowFromUid(packagename, uid)

            net_end_rx = net_bck_end_rx + net_front_end_rx
            net_end_tx = net_bck_end_tx + net_front_end_tx
            lo_end_rx = lo_bck_end_rx + lo_front_end_rx
            lo_end_tx = lo_bck_end_tx + lo_front_end_tx
            
            net_flow_rx, net_flow_tx = net_end_rx - net_start_rx, net_end_tx - net_start_tx
            lo_flow_rx, lo_flow_tx = lo_end_rx - lo_start_rx, lo_end_tx - lo_start_tx
            net_rx_kb, net_tx_kb = round(net_flow_rx / 1024, 3), round(net_flow_tx / 1024, 3)
            lo_rx_kb, lo_tx_kb = round(lo_flow_rx / 1024, 3), round(lo_flow_tx / 1024, 3)
            #rx_mb, tx_mb = round(flow_rx / 1024 / 1024, 3), round(flow_tx / 1024 / 1024, 3)
            print(n,
                  '网络下行：', net_rx_kb, 'KB\t',
                  '网络上行：', net_tx_kb, 'KB\t',
                  '网络总流量', round(net_rx_kb + net_tx_kb, 3), 'KB\t\t',
                  '本地下行：', lo_rx_kb, 'KB\t',
                  '本地上行：', lo_tx_kb, 'KB\t',
                  '本地总流量', round(lo_rx_kb + lo_tx_kb, 3), 'KB\t'
                  )
            if n == LIMIT:
                break
        except KeyboardInterrupt:
            break

    print(
        '统计时长：%d s' % LIMIT
    )
    # print(
    #     '实际下行流量：', rx_mb, 'MB\t',
    #     '实际上行流量：', tx_mb, 'MB\t',
    #     '实际总流量', round(rx_mb + tx_mb, 3), 'MB\t'
    # )
