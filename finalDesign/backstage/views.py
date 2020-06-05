from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Menu, Member, Menu_Order, Order, Restaurant
# Create your views here.


# 登录页面跳转
def login(request):
    return render(request, 'login.html')


# 首页跳转
def index(request):
    return render(request, 'index.html')


# 菜单信息查询
def menu(request):
    foods = Menu.menuObj.all()
    return render(request, 'menu.html', {"foods": foods})


# 已处理订单查询
def order1(request):
    orders = Order.objects.filter(finish=1)
    return render(request, 'order1.html', {"orders": orders})


# 未处理订单查询
def order2(request):
    orders = Order.objects.filter(finish=0)
    return render(request, 'order2.html', {"orders": orders})


# 用户信息查询
def member(request):
    members = Member.objects.all()
    return render(request, 'member.html', {"members": members})


# 添加菜品页面跳转
def addmenu(request):
    return render(request, 'addmenu.html')


# 添加菜品信息
def addmenu1(request):
    name = request.POST.get("name")
    pirture = request.POST.get("picture")
    category = request.POST.get("category")
    price = request.POST.get("price")
    integral = request.POST.get("integral")
    valid = request.POST.get("valid")
    food = Menu.menuObj.createmenu(name, pirture, category, price, integral, valid)
    food.save()
    # return redirect('/backstage/menu')
    return HttpResponse('sadfasfd')


# 更改菜品信息跳转
def updatamenu(request):
    menuid = request.GET.get("id")
    food = Menu.menuObj.get(pk=menuid)
    return render(request, 'updatamenu.html', {'food': food})


# 更改菜品信息之更改
def finish_updatamenu(request):
    name = request.POST.get('name')
    img = request.POST.get('img')
    category = request.POST.get('category')
    price = request.POST.get('price')
    integral = request.POST.get('integral')
    valid = request.POST.get('valid')
    foodid = request.POST.get('id')
    food = Menu.menuObj.get(pk=foodid)
    food.menu_name = name
    food.picture = img
    food.category = category
    food.menu_price = price
    food.menu_integral = integral
    food.valid = valid
    food.save()
    return redirect('/backstage/menu')


# 更改订单信息之跳转
def updataorder(request):
    orderid = request.GET.get('id')
    order = Order.objects.get(id=orderid)
    return render(request, 'updataorder.html', {"order": order})


# 更改订单信息之更改
def finish_upadataorder(request):
    table = request.POST.get("table_id")
    server = request.POST.get("server_id")
    price = request.POST.get("price")
    finish = request.POST.get('finish')
    orderid = request.POST.get('order_id')
    order = Order.objects.get(pk=orderid)
    order.table = table
    order.server = server
    order.price = price
    order.finish = finish
    order.save()
    return redirect("/backstage/order2")


# 更改用户信息之跳转
def updatamember(request):
    memberid = request.GET.get('id')
    member = Member.objects.get(id=memberid)
    return render(request, 'updatamember.html', {"member": member})


# 更改用户信息之更改
def finishi_updatamember(request):
    name = request.POST.get("name")
    integral = request.POST.get('integral')
    isVIP = request.POST.get('isVIP')
    member_id = request.POST.get('member_id')
    member = Member.objects.get(pk=member_id)
    member.member_name = name
    member.member_integral = integral
    member.isVIP = isVIP
    member.save()
    return redirect("/backstage/member")


# 后台登录
def login2(request):
    account = request.POST.get("userid")
    password = request.POST.get("psw")
    if account == '':
        return HttpResponse('请输入正确账号')
    else:
        account1 = Restaurant.objects.get(account=account)
        if account1.password == password:
            return redirect('/backstage/index')
        else:
            return HttpResponse('请输入正确密码')


# 查看订单详情
def orderinfo(request):
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
                    'food_num': food_num,
        }
        list.append(text)
        print(menu)
    print(list)

    return render(request, 'orderinfo.html', {'list': list})


# 精细化宝报表
def statistical(request):
    month = request.POST.get('month')
    data = Order.objects.filter(time__month=month, finish=1)
    month_statistic = 0
    for i in data:
        month_statistic += i.price
    return render(request, 'statistical.html', {'month_statistic': month_statistic})
