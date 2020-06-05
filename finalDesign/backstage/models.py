from django.db import models

# Create your models here.


class MenuManager(models.Manager):
    def createmenu(self, name, picture, category, menu_price, menu_integral, valid):
        food = self.model()
        food.menu_name = name
        food.picture = picture
        food.category = category
        food.menu_price = menu_price
        food.menu_integral = menu_integral
        food.valid = valid
        return food


class Menu(models.Model):
    menuObj = MenuManager()
    menu_name = models.CharField(max_length=20)
    picture = models.CharField(max_length=300)
    category = models.CharField(max_length=50)
    menu_price = models.FloatField()
    menu_integral = models.IntegerField()
    valid = models.BooleanField(default=True)

    class Meta:
        db_table = 'Menu'

    def __str__(self):
        return self.menu_name


class Member(models.Model):
    # 创建一个用户
    @classmethod
    def createMember(cls, name, photo, phone=0, integral=0, isVIP=0):
        mem = cls(member_name=name, photo=photo, phone=phone, member_integral=integral, isVIP=isVIP)
        return mem

    member_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=50)
    member_integral = models.IntegerField(default=0)
    photo = models.CharField(max_length=300)
    isVIP = models.IntegerField(default=0)

    class Meta:
        db_table = 'Member'


class Order(models.Model):
    # 定义一个方法创建订单
    @classmethod
    def createOrder(cls, time, price, member, table=0, server=0, finish=0):
        ord = cls(time=time, price=price, member=member, table=table, server=server, finish=finish)
        return ord

    member = models.ForeignKey("Member", on_delete=models.CASCADE, default=1)
    time = models.DateTimeField(auto_now_add=True)
    table = models.IntegerField(default=0)
    server = models.IntegerField(default=0)
    price = models.FloatField()
    finish = models.IntegerField(default=0)


    class Meta:
        db_table = 'Order'
        ordering = ['-time']


class Menu_Order(models.Model):
    # 定义方法创建对象
    @classmethod
    def createMenu_Order(cls, order_id, menu_id, food_num):
        mo = cls(order=order_id, menu=menu_id, food_num=food_num)
        return mo

    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    food_num = models.IntegerField()

    class Meta:
        db_table = 'Menu_Order'


class Restaurant(models.Model):
    wechat_num = models.CharField(max_length=50)
    account = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    valid = models.IntegerField()

    class Meta:
        db_table = 'Restaurant'
