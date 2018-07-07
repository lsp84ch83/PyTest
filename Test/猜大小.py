# _*_ coding:utf-8 _*_

import random

guess = int(input('输入心中的数字：'))
secret = random.randint(1,100)
count = 3

while count:
    if guess == secret:
        print('恭喜猜对了！')
        break
    else:
        if guess > secret:
            print('你猜大了')
        else:
            print('你猜小了')
        count -= 1
        print('你还有%d次机会,请继续：' %count,end='')
        guess = int(input())

    if count == 1:
        break

if count == 1:
    print('游戏结束')
    print('随机数字是%d' %secret)
