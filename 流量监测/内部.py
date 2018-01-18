#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/17 21:54
# @Author  : Soner
# @version :
# @license : Copyright(C), Your Company

import time
import subprocess
import xlwt

def getUid(package_name):#获取UID
    cmd = 'adb shell dumpsys package ' + package_name + ' | findstr userId'
    p1 = subprocess.Popen(cmd, shell = True,
    stdout=subprocess.PIPE, stderr = subprocess.PIPE)#用adb获取信息
    uidLongString = str(p1.stdout.read().strip(), encoding="utf-8")
    uidLongList = uidLongString.split("=")
    uid = uidLongList[1]
    return uid[0:5]

def getRev(package_name):#获取某个APP的TCP下载流量
    p1 = subprocess.Popen('adb shell cd proc && cd uid_stat && cd '+ getUid(package_name) +' && cat tcp_rcv',
    stdout=subprocess.PIPE,stderr=subprocess.PIPE)#用adb获取信息uid
    flo_rec =int(p1.stdout.read())
    return  float("%.2f" % (flo_rec / 1000))

def getSnd(package_name):#获取某个APP的TCP上传流量
    p1 = subprocess.Popen('adb shell cd proc && cd uid_stat && cd '+ getUid(package_name) +' && cat tcp_snd',
    stdout=subprocess.PIPE,stderr=subprocess.PIPE)#用adb获取信息
    flo_snd =int(p1.stdout.read())
    return  float("%.2f" % (flo_snd / 1000))

time_end =86400 # 24个小时时间，单位秒
col =0
row =0

book_Mirror = xlwt.Workbook(encoding='utf-8',style_compression=0)#创建新的工作簿Mirror
book_Mirror_Server = xlwt.Workbook(encoding='utf-8',style_compression=0)#创建新的工作簿Mirror_Server
book_TXZ = xlwt.Workbook(encoding='utf-8',style_compression=0)#创建新的工作簿TXZ

sheet_load_sdk = book_Mirror.add_sheet('流量',cell_overwrite_ok=True)#创建新的sheet，并命名为LOAD
#sheet_upload_sdk = book_sdk.add_sheet('上传流量',cell_overwrite_ok=True)

sheet_load_wx = book_Mirror_Server.add_sheet('流量',cell_overwrite_ok=True)#创建新的sheet，并命名为LOAD
#sheet_upload_wx = book_wx.add_sheet('上传流量',cell_overwrite_ok=True)

sheet_load_TXZ = book_TXZ.add_sheet('流量',cell_overwrite_ok=True)#创建新的sheet，并命名为LOAD
#sheet_upload_wx = book_wx.add_sheet('上传流量',cell_overwrite_ok=True)

sheet_load_sdk.write(row,col,"时间")
sheet_load_sdk.write(row,col +1,"下载流量(KB)")
sheet_load_sdk.write(row,col +2,"上传流量(KB)")

sheet_load_wx.write(row,col,"时间")
sheet_load_wx.write(row,col +1,"下载流量(KB)")
sheet_load_wx.write(row,col +2,"上传流量(KB)")

sheet_load_TXZ.write(row,col,"时间")
sheet_load_TXZ.write(row,col +1,"下载流量(KB)")
sheet_load_TXZ.write(row,col +2,"上传流量(KB)")

# ----------------- 需要监测的包名 -----------------
package_name_Mirror="cn.hollo.mirror"
package_name_Mirror_Server ="cn.hollo.mirror.service"
package_name_TXZ ="com.txznet.txz"

try:
    uid_sdk = getUid(package_name_Mirror)
    print(time.strftime('%Y-%m-%d   %H:%M:%S',time.localtime(time.time())) +'  uid =  '+str(uid_sdk))
except:
    print('获取Mirror-uid失败')

try:
    uid_wx = getUid(package_name_Mirror_Server)
    print(time.strftime('%Y-%m-%d   %H:%M:%S',time.localtime(time.time())) +'  uid =  '+str(uid_wx))
except:
    print('获取Mirror_Server-uid失败')

try:
    uid_wx = getUid(package_name_TXZ)
    print(time.strftime('%Y-%m-%d   %H:%M:%S',time.localtime(time.time())) +'  uid =  '+str(uid_wx))
except:
    print('获取TXZ-uid失败')

row =1
col =0

while   time_end > 0:

    load_sdk = getRev(package_name_Mirror)
    upload_sdk = getSnd(package_name_Mirror)

    load_wx = getRev(package_name_Mirror_Server)
    upload_wx = getSnd(package_name_Mirror_Server)

    load_TXZ = getRev(package_name_TXZ)
    upload_TXZ = getSnd(package_name_TXZ)

    timeNow = time.strftime('%Y-%m-%d   %H:%M:%S',time.localtime(time.time()))#获取当前时间

    sheet_load_sdk.write(row,col,timeNow)#写入时间
    sheet_load_sdk.write(row,col +1,load_sdk)#写入下载流量
    sheet_load_sdk.write(row,col +2,upload_sdk)#写入上传流量

    sheet_load_wx.write(row,col,timeNow)#写入时间
    sheet_load_wx.write(row,col +1,load_wx)#写入下载流量
    sheet_load_wx.write(row,col +2,upload_wx)#写入上传流量

    sheet_load_TXZ.write(row,col,timeNow)#写入时间
    sheet_load_TXZ.write(row,col +1,load_TXZ)#写入下载流量
    sheet_load_TXZ.write(row,col +2,upload_TXZ)#写入上传流量

    print("---------- %s ----------" % row)
    print(str(timeNow) +'  下载流量='+str(load_sdk)+"KB     " +'    上传流量='+str(upload_sdk)+"KB")
    print(str(timeNow) +'  下载流量='+str(load_wx)+"KB      " +'    上传流量='+str(upload_wx)+"KB")
    print(str(timeNow) +'  下载流量='+str(load_TXZ)+"KB     " +'    上传流量='+str(upload_TXZ)+"KB")

    row = row +1

    time.sleep(10)  # 控制监测频率
    time_end -=10
    if time_end <=0:
        print("---------- END ----------")
    book_Mirror.save(r"d:\MirrorFolw.xls")
    book_Mirror_Server.save(r"d:\Mirror_ServerFlow.xls")
    book_TXZ.save(r"d:\TXZFolw.xls")