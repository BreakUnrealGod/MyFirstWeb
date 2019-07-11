from django.shortcuts import render, redirect
import logging
import uuid
from time import sleep

from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.decorators.cache import cache_page
from django.core.cache import cache

from user.forms import RegisterForm, LoginForm
from user.models import User
# from user.task import sendmail
# from user.utils import login_required
# Create your views here.

#　首页
def index(request):
    return render(request, 'index.html')

# 注册
def user_register(request):
    if request.method == 'GET':
        rform = RegisterForm()
        return render(request, '../../Web/templates/register.html', context={'form': rform})
    else:
        rform = RegisterForm(request.POST)
        if rform.is_valid():
            data = rform.cleaned_data
            username = data.get('username')
            password = data.get('password')
            repassword = data.get('repassword')
            email = data.get('email')
            if password == repassword:
                password = make_password(password)
                user = User.objects.create(username=username, password=password)
                if user:
                    # 发送激活邮件
                    # uid = str(uuid.uuid4()).replace('-', '')
                    # cache.set(uid, user)
                    # print('uid:', uid)
                    # # 此时启动异步发送邮件
                    # result = sendmail.delay(uid, email)
                    # return HttpResponse('用户注册成功,赶快去激活吧！')
                    # return redirect('user:login', context={'form': rform, 'msg': '注册成功，请登录！'})
                    return HttpResponseRedirect('login')
            return render(request, '../../Web/templates/register.html', context={'form': rform, 'msg': '注册失败，重写注册'})

# 登录
def user_login(request):
    if request.method == 'GET':
        lform = LoginForm()
        return render(request, '../../Web/templates/login.html', context={'form': lform})
    # else:
    #     lform = LoginForm(request.POST)
    #     if lform.is_valid():
    #         data = lform.cleaned_data
    #         user = User.objects.filter(username=data.get('username')).first()
    #
    #         # password = lform.cleaned_data.get('password')
    #         # user = User.objects.filter(username=username).first()
    #         flag = check_password(data.get('password'), user.password)
    #         if user and user.is_active:
    #             flag = check_password(data.get('password'), user.password)
    #             if flag:
    #                 # token 令牌
    #                 # uid = uuid.uuid4()
    #                 # token = str(uid).replace('-', '')
    #                 # print("++++++++>token :", token)
    #                 # cache.set(token, user, timeout=60 * 30)
    #
    #                 # 创建response对象
    #                 # request.session['username'] = username
    #                 # return redirect('user:index', context={'form': lform})
    #                 # return HttpResponseRedirect('/')
    #                 # return render(request, '../../Web/templates/login.html', context={'form': lform, 'msg': '用户名或者密码有误！'})
    #                 username = lform.cleaned_data.get('username')
    #                 request.session['username'] = username
    #                 return HttpResponseRedirect('/')
    #         else:
    #             return render(request, '../../Web/templates/login.html', context={'form': lform, 'msg': '请检查用户名或者用户没有激活！'})
    #     return render(request, '../../Web/templates/login.html', context={'form': lform, 'msg': '用户名或者密码有误！'})
    else:
        lform = LoginForm(request.POST)
        if lform.is_valid():
            username = lform.cleaned_data.get('username')
            password = lform.cleaned_data.get('password')
            user = User.objects.filter(username=username).first()
            flag = check_password(password, user.password)
            if flag:
                # 保存session信息
                username = lform.cleaned_data.get('username')
                request.session['username'] = username
                return HttpResponseRedirect('/')
        else:
            return render(request, '../../Web/templates/login.html', context={'form': lform, 'msg': '请检查用户名或者用户没有激活！'})
    return render(request, '../../Web/templates/login.html', context={'form': lform, 'msg': '用户名或者密码有误！'})

# 用户注销
def user_logout(request):
    request.session.clear()  # 删除字典
    request.session.flush()  # 删除django_session + cookie +字典
    return HttpResponseRedirect('/')

# 进入个人中心
def user_center(request):
    username = request.session.get('username')
    user = User.objects.filter(username=username).first()
    print(user)
    username = user.username
    password = user.password
    email = user.email
    return render(request, '../../Web/templates/usercenter.html', context={'username': username, 'password': password, 'email': email})

#　修改密码
def update_password(request):
    if request.method == 'GET':
        rform = RegisterForm()
        return render(request, 'updatepassword.html', context={'form': rform})
    # else:
    #     code = request.POST.get('code')
    #     uid = request.session.get(code)
    #     user = UserProfile.objects.get(pk=uid)
    #     # 获取密码
    #     pwd = request.POST.get('password')
    #     repwd = request.POST.get('repassword')
    #     if pwd == repwd and user:
    #         pwd = make_password(pwd)
    #         user.password = pwd
    #         user.save()
    #         return render(request, 'user/update_pwd.html', context={'msg': '用户密码更新成功！'})
    #     else:
    #         return render(request, 'user/update_pwd.html', context={'msg': '更新失败！'})
    else:
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')

        username = request.session.get('username')
        user = User.objects.filter(username=username).first()
        if new_password1 == new_password2:
            new_password1 = make_password(new_password1)
            user.password = new_password1
            user.save()
            request.session.clear()  # 删除字典
            request.session.flush()  # 删除django_session + cookie +字典
            return HttpResponseRedirect('login')

        else:
            return render(request, 'updatepassword.html', context={'msg': '更新失败！'})

# def user_game(request):
#     return render(request, 'usergame.html')

#背景图片
def user_background(request):
    return render(request, 'userbackground.html')















