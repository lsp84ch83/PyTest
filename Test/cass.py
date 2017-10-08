# -*- coding:utf-8 -*-

class Vehicle:
    def __init__(self,speed):
        self.speed = speed

    def drive(self,distance):
        print 'need %.2f hour(s)' % (distance / self.speed)

class Bike(Vehicle):
    pass

class Car(Vehicle):
    def __init__(self,speed,fuel):
        Vehicle.__init__(self,speed)
        self.fuel = fuel

    def drive(self,distance):
        Vehicle.drive(self,distance)
        print 'need %.2f fuels' % (distance * self.fuel)


b = Bike(input('输入自行车的每小时速度：'))
c = Car(input('输入小汽车的每小时速度：'),input('输入小汽车的每小时耗油：'))
b.drive(input('\n' + '输入自行车的总里程:'))
c.drive(input('\n' + '输入小汽车的总里程:'))
