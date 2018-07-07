# _*_ coding:utf-8 _*_

num = int(input('输入任意大于0的数字：'))

while num:
    print(' ' * (num-1) + '*' * num)
    num -= 1
