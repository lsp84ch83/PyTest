# -*- coding: utf-8 -*-

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
        s = smtplib.SMTP()  
        s.connect("smtp.163.com") #这里我使用的是阿里云邮箱,也可以使用163邮箱：smtp.163.com  
        s.login(sender, passwd)  
        s.sendmail(sender, receivers, msgRoot.as_string())  
        print ("邮件发送成功")  
    except smtplib.SMTPException as e:  
        print("Error, 发送失败")  
    finally:  
        s.quit()  

subject = "流量监测"  
content = "附件为后视镜产品相关APP的流量监测使用情况"  
jpg_path = "d:\\test\\Mirror_Folw_%s.xls" %time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time()))  
pdf_path = "d:\\test\\Mirror_Server_Folw_%s.xls" %time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time()))  
txt_path = "d:\\test\\Mirror_Txz_Folw_%s.xls" %time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time())) 
file_path = [jpg_path,pdf_path,txt_path]  #发送三个文件到两个邮箱  
receive_email = ["317152347@QQ.com"]  
Send_email_text(subject,content,file_path,receive_email)  
