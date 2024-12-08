"""a_django_basic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView, RedirectView

from . import views
from .views import MyView

"""
    补充解释:
    1. url.py 如果写/, e.g path('index/', views.index); get请求因为会在请求path结尾自动添加/(P.S Post不行), 所以浏览器访问时.
    - localhost:8000/index
    - localhost:8000/index/ 均可匹配
    但是ajax请求不会自动添加/, 此时请求需要写准确, 即localhost:8000/index/

    2. url.py 如果不写/, e,g path('index', views.index); 无论哪种请求都必须要按照设定书写才行, localhost:8000/index
"""

# 可能的请求情况放在该列表中, django会自动匹配每种请求情况对应的处理方法.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),

    # 当请求 func1/ 时, 将该请求交给views模块下的func1的函数处理.
    # 第一个参数匹配URL中的path部分(端口后, 参数前的内容)
    path('func1/', views.func1),

    # 匹配localhost:8000
    path('', views.func2),

    # 补充: 第一个参数是否加 / 的问题. 参考上面补充解释
    path('func3', views.func3),

    # 匹配一类请求path, sport/str/
    # 转换器收集到的字符串传递给视图函数的country的形参名字.
    path('sport/<str:country>/', views.func4),

    #     英文字符串     数字       路径
    path('<slug:name>/<int:age>/<path:info>/', views.func5),

    # http请求的解析
    path('request/', views.handle_request),
    path('regist/', views.regist),

    # http响应的处理
    path('response/', views.handle_response),
    path('response/child', views.handle_response_child),

    # 通用视图使用
    path('templateView/', TemplateView.as_view(template_name='TemplateView.html')),
    path('daxin/', RedirectView.as_view(url='/templateView/')),

    path('myview/<str:name>/', MyView.as_view()),

]
