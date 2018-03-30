from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event,Guest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



# Create your views here.

def  index(request):
    return render(request, "index.html")


#  登录动作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)   # 登录
            #response.set_cookie('user', username, 3600)     # 添加浏览器 cookie
            request.session['user'] = username  #将session 信息记录到浏览器
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request, 'index.html', {'error': '账号或密码错误!'})


#  发布会管理
@login_required
def event_manage(request):
    event_list = Event.objects.all()
    username = request.session.get('user', '')
    return  render(request, 'event_manage.html', {'user': username,
                                                  'events': event_list})
#  发布会名称搜索
@login_required
def search_name(request):
    username = request.session.get('user', '')
    search_name = request.GET.get('name', '')
    event_list = Event.objects.filter(name__contains = search_name)
    return  render(request, 'event_manage.html', {'user': username,
                                                  'events':event_list})

#  签到页面
@login_required
def sign_index(request, eid):
    event = get_object_or_404(Event, id = eid)
    return render(request, 'sign_index.html', {'event': event})

#  签到动作
@login_required
def sign_index_action(request, eid):
    event = get_object_or_404(Event, id =eid)
    phone = request.POST.get('phone', '')
    print(phone)
    result = Guest.objects.filter(phone = phone)
    if not result:
        return render(request, 'sign_index.html', {'event': event,
                                                   'hint': '手机号不存在.'})
    result = Guest.objects.filter(phone = phone, event_id = eid)
    if not result:
        return render(request, 'sign_index.html', {'event': event,
                                                   'hint': '未参与的手机号.'})
    result = Guest.objects.get(phone = phone, event_id = eid)
    if result.sign:
        return render(request, 'sign_index.html', {'event': event,
                                                   'hint': '重复签到.'})
    else:
        Guest.objects.filter(phone = phone, event_id = eid).update(sign = '1')
        return render(request, 'sign_index.html', {'event': event,
                                                   'hint': '签到成功!',
                                                   'guest': result})



#  嘉宾管理
@login_required
def guest_manage(request):
    guest_list = Guest.objects.all()
    username = request.session.get('user', '')
    paginator = Paginator(guest_list, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果 page 不是整数，取第一页面数据
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果 page 不在范围内，取最后一页面
        contacts = paginator.page(paginator.num_pages)

    return  render(request, 'guest_manage.html', {'user': username,
                                                  'guests': contacts})
#  嘉宾名称搜索
@login_required
def search_rename(request):
    username = request.session.get('user', '')
    search_rename = request.GET.get('realname', '')     # 通过 requests 的 get() 方法获取 realname
    guest_list = Guest.objects.filter(realname__contains = search_rename)   # 将 realname 作为过滤条件，获取指定名称的数据列表
    paginator = Paginator(guest_list, 2)    # 将过滤结果按每页2条进行分页
    page = request.GET.get('page')      # 通过GET 请求得到当前要实现第几页的数据
    try:
        contacts = paginator.page(page) # 获取第page 页的数据
    except PageNotAnInteger:
        contacts = paginator.page(1)    # 如果 page 不是整数，取第一页面数据
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)  # 如果 page 不在范围内，取最后一页面
    return  render(request, 'guest_manage.html', {'user': username,
                                                  'guests': contacts,
                                                  'search_rename': search_rename})  # 返回搜索关键词