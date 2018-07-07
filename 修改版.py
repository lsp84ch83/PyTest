#!/usr/bin/env python
# _*_ coding: utf-8 _*_
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
import threading

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
      
    ##添加附件格式部分
    for path in filepath:
        if ".jpg" in path:  
            #jpg类型附件  
            jpg_name = path.split("\\")[-1]  
            part = MIMEApplication(open(path,'rb').read())   
            part.add_header('Content-Disposition', 'attachment', filename=jpg_name)  
            msgRoot.attach(part)  
          
        if ".pdf" in path:  
            #pdf类型附件  
            pdf_name = path.split("\\")[-1]  
            part = MIMEApplication(open(path,'rb').read())   
            part.add_header('Content-Disposition', 'attachment', filename=pdf_name)   
            msgRoot.attach(part)  
          
        if ".xls" in path:  
            #xlsx类型附件  
            xlsx_name = path.split("\\")[-1]  
            part = MIMEApplication(open(path,'rb').read())   
            part.add_header('Content-Disposition', 'attachment', filename=xlsx_name)  
            msgRoot.attach(part)  
              
        if ".txt" in path:  
            #txt类型附件  
            txt_name = path.split("\\")[-1]  
            part = MIMEApplication(open(path,'rb').read())  
            part.add_header('Content-Disposition', 'attachment', filename=txt_name)  
            msgRoot.attach(part)  
          
        if ".mp3" in path:  
            #mp3类型附件  
            mp3_name = path.split("\\")[-1]  
            part = MIMEApplication(open(path,'rb').read())   
            part.add_header('Content-Disposition', 'attachment', filename=mp3_name)   
            msgRoot.attach(part)
    
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

class Mymail(threading.Thread):
    def __init__(self, threadID,time_d, i):
         threading.Thread.__init__(self)
         self.threadID = threadID
         self.i = i
         self.time_d = time_d

    def run(self):
         threadLock.acquire()  # 获得锁
         if self.time_d == (30 * self.i):
             t = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
             shutil.copy("流量.xls", "f:\\test\\流量_Folw_%s.xls" %t)

             subject = "设计费拉上流量监测"
             content = "返回到顺丰到付附件为后视镜产品相关APP的流量监测使用情况"
             Mirror_path = "f:\\test\\流量_Folw_%s.xls" %t
             file_path = [Mirror_path]  #发送三个文件到两个邮箱
             receive_email = ["317152347@QQ.com"]
             Send_email_text(subject,content,file_path,receive_email)
             print("第%s个半小时保存备份成功" % str(self.i))
             self.i += 1
         self.time_d += 10
         threadLock.release()  # 释放锁

# ----------------- 创建EXCEL表格 -----------------
class MyThread(threading.Thread):
    def __init__(self,threadID, package_name,book_Mirror):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.package_name = package_name
        self.book_Mirror = book_Mirror

    def run(self):
        col =0
        row =0
        sheet_load_Mirror = self.book_Mirror.add_sheet(self.package_name, cell_overwrite_ok=True)  # 创建新的sheet
        sheet_load_Mirror.write(row, col, "时间")
        sheet_load_Mirror.write(row, col + 1, "网络下行(KB)")
        sheet_load_Mirror.write(row, col + 2, "网络上行(KB)")
        sheet_load_Mirror.write(row, col + 3, "网络总流量(KB)")
        sheet_load_Mirror.write(row, col + 4, "本地下行(KB)")
        sheet_load_Mirror.write(row, col + 5, "本地上行(KB)")
        sheet_load_Mirror.write(row, col + 6, "本地总流量(KB)")

        global time_end
        time_end =0 # 监测时间是72个小时时间，单位秒
        uid = (getUid(self.package_name))[0:5]
        try:
            uid_sdk = getUid(self.package_name)
            print(time.strftime('%Y-%m-%d   %H:%M:%S',time.localtime(time.time())) +'  uid =  '+str(uid_sdk))
        except:
            print('获取Mirror-uid失败')

        # ----------------- 获取初始流量 -----------------
        file_dir = "F:\\"
        os.chdir(file_dir)

        net_bck_start_rx, net_front_start_rx, net_bck_start_tx, net_front_start_tx, \
        lo_bck_start_rx, lo_front_start_rx, lo_bck_start_tx, lo_front_start_tx = getFlowFromUid(self.package_name, uid)

        net_start_rx = net_bck_start_rx + net_front_start_rx
        net_start_tx = net_bck_start_tx + net_front_start_tx
        lo_start_rx = lo_bck_start_rx + lo_front_start_rx
        lo_start_tx = lo_bck_start_tx + lo_front_start_tx

        row =1
        col =0
        i = 1
        while   time_end <= 259200:
            threadLock.acquire()    # 获得锁

            net_bck_end_rx, net_front_end_rx, net_bck_end_tx, net_front_end_tx, \
            lo_bck_end_rx, lo_front_end_rx, lo_bck_end_tx, lo_front_end_tx = getFlowFromUid(self.package_name, uid)

            net_end_rx = net_bck_end_rx + net_front_end_rx
            net_end_tx = net_bck_end_tx + net_front_end_tx
            lo_end_rx = lo_bck_end_rx + lo_front_end_rx
            lo_end_tx = lo_bck_end_tx + lo_front_end_tx

            net_flow_rx, net_flow_tx = net_end_rx - net_start_rx, net_end_tx - net_start_tx
            lo_flow_rx, lo_flow_tx = lo_end_rx - lo_start_rx, lo_end_tx - lo_start_tx
            net_rx_kb, net_tx_kb = round(net_flow_rx / 1024, 3), round(net_flow_tx / 1024, 3)
            lo_rx_kb, lo_tx_kb = round(lo_flow_rx / 1024, 3), round(lo_flow_tx / 1024, 3)

            # ----------------- 写入EXCEL表格 -----------------
            timeNow = time.strftime('%Y-%m-%d   %H:%M:%S', time.localtime(time.time()))  # 获取当前时间
            sheet_load_Mirror.write(row, col, timeNow)  # 写入时间
            sheet_load_Mirror.write(row, col + 1, net_rx_kb)  # 写入网络下行(KB)
            sheet_load_Mirror.write(row, col + 2, net_tx_kb)  # 写入网络上行(KB)
            sheet_load_Mirror.write(row, col + 3, round(net_rx_kb + net_tx_kb, 3))  # 写入网络总流量(KB)
            sheet_load_Mirror.write(row, col + 4, lo_rx_kb)  # 写入本地上行(KB)
            sheet_load_Mirror.write(row, col + 5, lo_tx_kb)  # 写入本地下行(KB)
            sheet_load_Mirror.write(row, col + 6, round(lo_rx_kb + lo_tx_kb, 3))  # 写入本地总流量(KB)
            self.book_Mirror.save(r"f:\流量.xls")

            threadLock.release()    # 释放锁

            print(" %s ---------- %s %s ----------" %(row, self.package_name, time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time()))))
            print(
                  '网络下行：', net_rx_kb, 'KB\t',
                  '网络上行：', net_tx_kb, 'KB\t',
                  '网络总流量', round(net_rx_kb + net_tx_kb, 3), 'KB\t\t',
                  '本地下行：', lo_rx_kb, 'KB\t',
                  '本地上行：', lo_tx_kb, 'KB\t',
                  '本地总流量', round(lo_rx_kb + lo_tx_kb, 3), 'KB\t\n'
                  )

            # if time_end == (30 * i):
            #     global t
            #     t = time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time()))
            #     shutil.copy("流量.xls", "f:\\test\\流量_Folw_%s.xls" %t)
            #     '''
            #     p = 0
            #     if p == 0:
            #         subject = "设计费拉上流量监测"
            #         content = "返回到顺丰到付附件为后视镜产品相关APP的流量监测使用情况"
            #         Mirror_path = "f:\\test\\流量_Folw_%s.xls" %t
            #         file_path = [Mirror_path]  #发送三个文件到两个邮箱
            #         receive_email = ["317152347@QQ.com"]
            #         Send_email_text(subject,content,file_path,receive_email)
            #         # sen_mail = Mymail(i, t)
            #         # sen_mail.start()
            #         p += 1
            #
            #     # subject = "设计费拉上流量监测"
            #     # content = "返回到顺丰到付附件为后视镜产品相关APP的流量监测使用情况"
            #     # Mirror_path = "f:\\test\\流量_Folw_%s.xls" %time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time()))
            #     # file_path = [Mirror_path]  #发送三个文件到两个邮箱
            #     # receive_email = ["317152347@QQ.com"]
            #     # Send_email_text(subject,content,file_path,receive_email)
            #     '''
            #     print("第%s个半小时保存备份成功" % str(i))
            #     i += 1
            row = row +1
            time.sleep(10)  # 控制监测频率
            time_end +=10

            if time_end <=0:
                print("---------- END ----------")


threadLock = threading.Lock()
threads = []
book_Mirror = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 创建新的工作簿Mirror


# 创建新线程
webchat = MyThread(1,'com.txznet.webchat',book_Mirror)
kwmusiccar = MyThread(2,'cn.kuwo.kwmusiccar',book_Mirror)
amap = MyThread(3,'com.autonavi.amapautolite',book_Mirror)
mirror = MyThread(4,'cn.hollo.mirror',book_Mirror)
mirror_server = MyThread(5,'cn.hollo.mirror.service',book_Mirror)
txz = MyThread(6,'com.txznet.txz',book_Mirror)
sen_mail = Mymail(4,0,1)

# 开启新线程
webchat.start()
kwmusiccar.start()
amap.start()
mirror.start()
mirror_server.start()
txz.start()
sen_mail.start()

# 添加线程到线程列表
threads.append(webchat)
threads.append(kwmusiccar)
threads.append(amap)
threads.append(mirror)
threads.append(mirror_server)
threads.append(txz)
threads.append(sen_mail)

# 等待所有线程完成
for k in threads:
    k.join()
