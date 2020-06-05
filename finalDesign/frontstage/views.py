from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from rest_framework import serializers
from backstage.models import Menu, Member, Menu_Order, Order
from datetime import datetime


# 获取菜单信息
def menuInfo(request):
    try:
        menu = Menu.menuObj.filter(valid=True)
        list = []
        for i in menu:
            text = {
                'category': i.category,
                    "child" : [
                        {
                            'id': i.id,
                            'menu_name': i.menu_name,
                            'picture': i.picture,
                            "menu_price": i.menu_price,
                            'menu_integral': i.menu_integral,
                            'valid': i.valid
                        }
                    ]
                }
            list.append(text)
        map = {}
        for i in list:
            if i["category"] in map:
                map[i["category"]].append(i["child"][0])
            else:
                map[i["category"]] = []
                map[i["category"]].append(i["child"][0])
        list = []
        for k, v in map.items():
            map_temp = {}
            map_temp["category"] = k
            map_temp["child"] = []
            for i in v:
                map_temp["child"].append(i)
            list.append(map_temp)
        return JsonResponse({"message": list})
    except Exception as e:
        return HttpResponse(e)


# 获取菜品详情
def foodInfo(request):
    try:
        id = request.GET.get("id")
        food = Menu.menuObj.get(pk=id)
        list = {
            'id': food.id,
            'name': food.menu_name,
            'picture': food.picture,
            'price': food.menu_price,
            'integral': food.menu_integral,
        }

        return JsonResponse({'message': list})
    except Exception as e:
        return HttpResponse(e)


# 生成订单
def createorder(request):
    try:
        if request.method == 'POST':
            userid = request.POST.get('userid')
            order_price = request.POST.get('order_price')
            timestamp = request.POST.get('timestamp')
            goods = request.POST.get('goods')
            json_data = json.loads(goods)
            mem = Member.objects.get(pk=userid)
            ord = Order.createOrder(timestamp, order_price, mem)
            i = int(order_price)
            ord.save()
            isVIP = mem.isVIP
            if isVIP:
                mem.member_integral += i
                print(mem.member_integral)
                mem.save()
                for i in json_data:
                    value_lits = i.values()
                    vl = list(value_lits)
                    menuid = vl[0]
                    menu = Menu.menuObj.get(pk=menuid)
                    foodnum = vl[1]
                    mn = Menu_Order.createMenu_Order(ord, menu, foodnum)
                    mn.save()
                return HttpResponse('支付成功')
            else:
                for i in json_data:
                    value_lits = i.values()
                    vl = list(value_lits)
                    menuid = vl[0]
                    menu = Menu.menuObj.get(pk=menuid)
                    foodnum = vl[1]
                    mn = Menu_Order.createMenu_Order(ord, menu, foodnum)
                    mn.save()
                return HttpResponse('支付成功')
    except Exception as e:
        return HttpResponse(e)


# 获取订单信息
def getOrderInfo(request):
    try:
        id = request.GET.get("userid")
        mem = Member.objects.get(pk=id)
        orders = Order.objects.filter(member_id=mem)
        list = []
        for i in orders:
            text = {
                "orderid": i.id,
                'orderprice': i.price,
                'time': i.time,
                'table': i.table,
            }
            list.append(text)
        return JsonResponse({'message': list})
    except Exception as e:
        return HttpResponse(e)


# 获取单个订单信息
def getOrder(request):
    try:
        orderid = request.GET.get('id')
        food = Order.objects.get(id=orderid)
        list=[
            {
                'table': food.table,
                'server': food.server,
                'totleprice': food.price,
                'time': food.time,
            }
        ]
        return JsonResponse({'message': list})
    except Exception as e:
        return HttpResponse(e)


# 查看订单详情
def orderinfo(request):
    try:
        orderid = request.GET.get('id')
        foods = Menu_Order.objects.filter(order__id__contains=orderid)
        list = []
        for i in foods:
            food_num = i.food_num
            menu = Menu.menuObj.get(pk=i.menu_id)
            text = {
                        'id': menu.id,
                        'menu_name': menu.menu_name,
                        'picture': menu.picture,
                        'price': menu.menu_price,
                        'food_num': food_num,
            }
            list.append(text)
        return JsonResponse({'message': list})
    except Exception as e:
        return HttpResponse(e)


# 菜品搜索
def qsearch(request):
    try:
        if request.method =='GET':
            content = request.GET.get('query')
            food = Menu.menuObj.filter(menu_name__contains=content)
            list=[]
            for i in food:
                text = {
                    'id': i.id,
                    'name': i.menu_name,
                }
                list.append(text)
            return JsonResponse({'message': list})
    except Exception as e:
        return HttpResponse(e)


# 小程序登录
def login(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            photo = request.POST.get('photo')
            mem = Member.objects.filter(member_name=name)
            if mem:
                userid = mem[0].id
                isVIP = mem[0].isVIP
                integral = mem[0].member_integral
                return JsonResponse({'userid': userid, 'isVIP': isVIP, 'integral': integral})
            else:
                mem1 = Member.createMember(name, photo)
                mem1.save()
                userid = mem1.id
                isVIP = mem1.isVIP
                integral = mem1.member_integral
                return JsonResponse({'userid': userid, 'isVIP': isVIP, 'integral': integral})
    except Exception as e:
        return HttpResponse(e)


# 每次进入登录页面更新isVIP 和 integral
def updatalogin(request):
    try:
       userid = request.GET.get('userid')
       user = Member.objects.get(pk=userid)
       isVIP = user.isVIP
       integral = user.member_integral
       return JsonResponse({'isVIP': isVIP, 'integral': integral})
    except Exception as e:
        return HttpResponse(e)


# 注册为会员
def sign(reqeuest):
    try:
        if reqeuest.method == 'POST':
            userid = reqeuest.POST.get('userid')
            phone = reqeuest.POST.get('userphone')
            int_phone = int(phone)
            mem = Member.objects.get(pk=userid)
            mem.phone = int_phone
            mem.isVIP = 1
            mem.save()
            return HttpResponse('修改成功')
    except Exception as e:
        return HttpResponse(e)
