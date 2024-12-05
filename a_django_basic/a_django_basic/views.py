from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, HttpResponseNotFound

# 引入settings中设置的变量
from django.conf import settings


def index(request):
    html = "<h1>%s</h1>" % settings.README
    return HttpResponse(html)


def func1(request):
    # 将html内容发送给浏览器显示
    return HttpResponse("<h1>func1</h1>")


def func2(request):
    return HttpResponse("<h1>func2</h1>")


def func3(request):
    return HttpResponse("<h1>func3</h1>")


def func4(request, country):
    res = {
        "china": "中国乒乓",
        "india": "印度乒乓",
    }
    return HttpResponse("<h1>%s</h1>" % res[country])


# path: http://localhost:8000/Jame-Green/18/boy/666/
def func5(request, name, age, info):
    # name: Jame-Green, age: 18, info: boy/666
    print("name: %s, age: %s, info: %s" % (name, age, info))
    return HttpResponse("<h1>func5</h1>")


# 解析http, request对象: 包含了请求的解析结果
def handle_request(request: HttpRequest):
    # 1. 获取请求url中的path部分; /request/
    print("1. path:", request.path_info)

    # 2. 获取请求类型; GET
    print("2. method:", request.method)

    # 3. 获取请求参数(都是字符串形式)
    # /request/?a=1&b=2 ==> <QueryDict: {'a': ['1'], 'b': ['2']}>
    # /request/?a=1&a=2&b=2 ==> <QueryDict: {'a': ['1', '2'], 'b': ['2']}>
    print("3. GET:", request.GET)  # 伪字典

    # 多选的GET请求并不是很友好, 多选建议用POST,request.GET["a"], request.GET.get("a")中对于多选只能取最后一个值.
    # /request/?a=1&b=2  ==> 1
    # /request/?a=1&a=2&b=2 ==> 2
    print("3. GET:", request.GET["a"])
    print("3. GET:", request.GET.get("a"))

    # /request/?a=1&b=2 ==> ['1']
    # /request/?a=1&a=2&b=2 ==> ['1', '2']
    print("3. GET:", request.GET.getlist("a"))

    # 如果没有c的参数, 返回null la
    # /request/?a=1&b=2 ==> null la
    # /request/?a=1&a=2&b=2 ==> null la
    print("3. GET:", request.GET.getlist("c", "null la"))

    # 4. 获取请求体内容
    # 表单提交, 与request.GET相同的字典.
    print("4.1 POST:", request.POST)

    # 以js等方式提交的POST请求体, 得到字节串.
    print("4.2 body:", request.body)

    # 5. 获取请求头内容 服务器系统基本的信息 + 请求头信息
    # 请求头转换: HTTP_请求头大写
    print("5.1 META:", request.META)
    print("5.2 META:", request.META.get("REMOTE_ADDR"))

    return HttpResponse("ok")


def regist(request: HttpRequest):
    if request.method == "GET":
        with open("templates/index.html", "r", encoding="utf-8") as fr:
            data = fr.read()

    elif request.method == "POST":
        username = request.POST.get("user")
        password = request.POST.get("pwd")
        print(username, password)
        data = "注册成功"

    return HttpResponse(data)


# http响应组织处理
def handle_response(request):
    # 方法1: 直接生成响应对象返回
    # response = HttpResponse(
    #     content="Hello World",  # 响应体
    #     status='200',  # 响应码
    #     content_type="text/html",  # 响应的数据类型
    #     headers={  # 其他响应头
    #         'Content-Length': 11
    #     }
    # )

    # # 方法2: 先生成响应对象, 后续再修改属性.
    response = HttpResponse()
    response.status_code = 200
    response.content = "Hello World2"
    response.content_type = "text/html"
    response.headers['Content-Length'] = 12

    return response


# HttpResponse子类
def handle_response_child(request):
    # 404响应
    # return HttpResponseNotFound(
    #     content="该页面不存在"
    # )

    # 302响应, 重定向
    return HttpResponseRedirect(
        redirect_to="/response/"
    )
