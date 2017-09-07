# -*- conding=utf-8 -*-
f = open('cj.txt',encoding='utf-8') #打开一个文件内容
lines = f.readlines() #按每行读取数据
#print(lines)    #打印读取的内容
f.close()   #关闭文件

results = []    #初始化一个列表

for line in lines:
    #print(line)
    data = line.split() #按条件‘’分隔每条数据
    #print(data) #显示分隔的数据

    sum = 0 #初始化求和
    for score in data[1:]:  #每条数据的第1个序列到最后为每次的数据
        sum += int(score)   #计算每个人的和
    result = '%s\t:%d' %(data[0],sum)
    #print(result)

    results.append('\n'+result) #写入求和的数据

#print(results)
output = open('cj.txt','a',encoding='utf-8')
output.writelines(results)
output.close()
