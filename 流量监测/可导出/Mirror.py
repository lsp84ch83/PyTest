#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/17 21:54
# @Author  : Soner
# @version :
# @license : Copyright(C), Your Company

import time
import subprocess
import xlwt
import os
import shutil
import datetime

# ----------------- 获取设备UID -----------------
def getUid(package_name):#获取UID
    cmd = 'adb shell dumpsys package ' + package_name + ' | findstr userId'
    p1 = subprocess.Popen(cmd, shell = True,
    stdout=subprocess.PIPE, stderr = subprocess.PIPE)#用adb获取信息
    uidLongString = str(p1.stdout.read().strip(), encoding="utf-8")
    uidLongList = uidLongString.split("=")
    uid = uidLongList[1]
    return uid[0:5]
# ----------------- 计算设备流量 -----------------
def getFlowFromUid(packagename, uid=None):
    '''
    # 通过应用uid，获取应用当前消耗的流量
    # return (rcv,snd)
    '''
    if uid is None:
        uid = getUid(packagename)
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

# ----------------- 发送邮件 -----------------
''''' 
函数说明：Send_email_text() 函数实现发送带有附件的邮件，可以群发，附件格式包括：xlsx,pdf,txt,jpg,mp3等 
参数说明： 
    1. subject：邮件主题 
    2. content：邮件正文 
    3. filepath：附件的地址, 输入格式为["","",...] 
    4. receive_email：收件人地址, 输入格式为["","",...] 
'''  
def Send_email_text(subject,content,filepath,receive_email):  
    import smtplib  
    from email.mime.multipart import MIMEMultipart   
    from email.mime.text import MIMEText   
    from email.mime.application import MIMEApplication  
    sender = "13521895260@163.com"  
    passwd = "lsp84ch83"  
    receivers = receive_email   #收件人邮箱  
      
    msgRoot = MIMEMultipart()   
    msgRoot['Subject'] = subject  
    msgRoot['From'] = sender  
      
    if len(receivers)>1:  
        msgRoot['To'] = ','.join(receivers) #群发邮件  
    else:  
        msgRoot['To'] = receivers[0]  
      
    part = MIMEText(content)   
    msgRoot.attach(part)  
      
    ##添加附件部分  
    for path in filepath:
        # if ".jpg" in path:
        #     #jpg类型附件
        #     jpg_name = path.split("\\")[-1]
        #     part = MIMEApplication(open(path,'rb').read())
        #     part.add_header('Content-Disposition', 'attachment', filename=jpg_name)
        #     msgRoot.attach(part)
        #
        # if ".pdf" in path:
        #     #pdf类型附件
        #     pdf_name = path.split("\\")[-1]
        #     part = MIMEApplication(open(path,'rb').read())
        #     part.add_header('Content-Disposition', 'attachment', filename=pdf_name)
        #     msgRoot.attach(part)
          
        if ".xls" in path:  
            #xlsx类型附件  
            xlsx_name = path.split("\\")[-1]  
            part = MIMEApplication(open(path,'rb').read())   
            part.add_header('Content-Disposition', 'attachment', filename=xlsx_name)  
            msgRoot.attach(part)  
              
        # if ".txt" in path:
        #     #txt类型附件
        #     txt_name = path.split("\\")[-1]
        #     part = MIMEApplication(open(path,'rb').read())
        #     part.add_header('Content-Disposition', 'attachment', filename=txt_name)
        #     msgRoot.attach(part)
        #
        # if ".mp3" in path:
        #     #mp3类型附件
        #     mp3_name = path.split("\\")[-1]
        #     part = MIMEApplication(open(path,'rb').read())
        #     part.add_header('Content-Disposition', 'attachment', filename=mp3_name)
        #     msgRoot.attach(part)
    
    try:
        global m
        m = smtplib.SMTP()  
        m.connect("smtp.163.com") #这里我使用的是阿里云邮箱,也可以使用163邮箱：smtp.163.com  
        m.login(sender, passwd)  
        m.sendmail(sender, receivers, msgRoot.as_string())  
        print("邮件发送成功")  
    except smtplib.SMTPException as e:  
        print("Error, 发送失败")  
    finally:  
        m.quit()

# ----------------- 创建EXCEL表格 -----------------
col =0
row =0

book_Mirror = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 创建新的工作簿Mirror

sheet_load_Mirror = book_Mirror.add_sheet('流量', cell_overwrite_ok=True)  # 创建新的sheet，并命名为LOAD

sheet_load_Mirror.write(row, col, "时间")
sheet_load_Mirror.write(row, col + 1, "网络下行(KB)")
sheet_load_Mirror.write(row, col + 2, "网络上行(KB)")
sheet_load_Mirror.write(row, col + 3, "网络总流量(KB)")
sheet_load_Mirror.write(row, col + 4, "本地下行(KB)")
sheet_load_Mirror.write(row, col + 5, "本地上行(KB)")
sheet_load_Mirror.write(row, col + 6, "本地总流量(KB)")


# ----------------- 需要监测的包名 -----------------
time_end =0 # 监测时间是72个小时时间，单位秒
package_name_Mirror= "cn.hollo.mirror"
uid = (getUid(package_name_Mirror))[0:5]
try:
    uid_sdk = getUid(package_name_Mirror)
    print(time.strftime('%Y-%m-%d   %H:%M:%S',time.localtime(time.time())) +'  uid =  '+str(uid_sdk))
except:
    print('获取Mirror-uid失败')

# ----------------- 定位文件目录 -----------------
file_dir = "D:\\"
os.chdir(file_dir)

row =1
col =0
s = 1
net_bck_start_rx, net_front_start_rx, net_bck_start_tx, net_front_start_tx, \
lo_bck_start_rx, lo_front_start_rx, lo_bck_start_tx, lo_front_start_tx = getFlowFromUid(package_name_Mirror, uid)

net_start_rx = net_bck_start_rx + net_front_start_rx
net_start_tx = net_bck_start_tx + net_front_start_tx
lo_start_rx = lo_bck_start_rx + lo_front_start_rx
lo_start_tx = lo_bck_start_tx + lo_front_start_tx

i = 1
time_k,time_s = 0,0

while   time_end <= 259200:

    net_bck_end_rx, net_front_end_rx, net_bck_end_tx, net_front_end_tx, \
    lo_bck_end_rx, lo_front_end_rx, lo_bck_end_tx, lo_front_end_tx = getFlowFromUid(package_name_Mirror, uid)

    net_end_rx = net_bck_end_rx + net_front_end_rx
    net_end_tx = net_bck_end_tx + net_front_end_tx
    lo_end_rx = lo_bck_end_rx + lo_front_end_rx
    lo_end_tx = lo_bck_end_tx + lo_front_end_tx

    net_flow_rx, net_flow_tx = net_end_rx - net_start_rx, net_end_tx - net_start_tx
    lo_flow_rx, lo_flow_tx = lo_end_rx - lo_start_rx, lo_end_tx - lo_start_tx
    net_rx_kb, net_tx_kb = round(net_flow_rx / 1024, 3), round(net_flow_tx / 1024, 3)
    lo_rx_kb, lo_tx_kb = round(lo_flow_rx / 1024, 3), round(lo_flow_tx / 1024, 3)

    timeNow = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))  # 获取当前时间
    timenew = time.strftime('%Y-%m-%d %H-%M', time.localtime(time.time()))  # 获取当前时间

    sheet_load_Mirror.write(row, col, timeNow)  # 写入时间
    sheet_load_Mirror.write(row, col + 1, net_rx_kb)  # 写入网络下行(KB)
    sheet_load_Mirror.write(row, col + 2, net_tx_kb)  # 写入网络上行(KB)
    sheet_load_Mirror.write(row, col + 3, round(net_rx_kb + net_tx_kb, 3))  # 写入网络总流量(KB)
    sheet_load_Mirror.write(row, col + 4, lo_rx_kb)  # 写入本地上行(KB)
    sheet_load_Mirror.write(row, col + 5, lo_tx_kb)  # 写入本地下行(KB)
    sheet_load_Mirror.write(row, col + 6, round(lo_rx_kb + lo_tx_kb, 3))  # 写入本地总流量(KB)
    book_Mirror.save("d:\Mirror_Folw.xls")
    print(" %s ---------- %s %s ----------" % (row, package_name_Mirror, timeNow))
    print(
          '网络下行：', net_rx_kb, 'KB\t',
          '网络上行：', net_tx_kb, 'KB\t',
          '网络总流量', round(net_rx_kb + net_tx_kb, 3), 'KB\t\t',
          '本地下行：', lo_rx_kb, 'KB\t',
          '本地上行：', lo_tx_kb, 'KB\t',
          '本地总流量', round(lo_rx_kb + lo_tx_kb, 3), 'KB\t\n'
          )

    row = row + 1
    time.sleep(10)  # 控制监测频率
    time_end += 10
    time_s += 10
    time_k += 10

    # 定时备份
    if time_s == 300:
        shutil.copy("Mirror_Folw.xls", "d:\\test\\Mirror_Folw_%s.xls" % timenew)
        shutil.copy("Mirror_Server_Folw.xls", "d:\\test\\Mirror_Server_Folw_%s.xls" % timenew)
        shutil.copy("Mirror_Txz_Folw.xls", "d:\\test\\Mirror_Txz_Folw_%s.xls" % timenew)
        shutil.copy("Amapautolite_Folw.xls", "d:\\test\\Amapautolite_Folw_%s.xls" % timenew)
        shutil.copy("Kwmusiccar_Folw.xls", "d:\\test\\Kwmusiccar_Folw_%s.xls" % timenew)
        shutil.copy("Webchat_Folw.xls", "d:\\test\\Webchat_Folw_%s.xls" % timenew)
        time_s = 0
        print('备份成功~！')

    try:
        # 定时发送邮件
        if time_end == (1800 * i):
            subject = "流量监测-拆分协议"
            content = "附件为后视镜拆分协议产品相关APP的流量监测使用情况"

            Mirror_path = "d:\\test\\Mirror_Folw_%s.xls" % timenew
            Server_path = "d:\\test\\Mirror_Server_Folw_%s.xls" % timenew
            Txz_path = "d:\\test\\Mirror_Txz_Folw_%s.xls" % timenew
            Amap_path = "d:\\test\\Amapautolite_Folw_%s.xls" % timenew
            Kuwo_path = "d:\\test\\Kwmusiccar_Folw_%s.xls" % timenew
            Webchat_path = "d:\\test\\Webchat_Folw_%s.xls" % timenew

            file_path = [Mirror_path,Server_path,Txz_path,Amap_path,Kuwo_path,Webchat_path]  #发送三个文件到两个邮箱
            receive_email = ["317152347@QQ.com"]
            Send_email_text(subject,content,file_path,receive_email)
            i += 1
    except:
        continue
print("---------- END  统计时长：%s----------" % str(time_k))