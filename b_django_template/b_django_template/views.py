from django.shortcuts import render


# 返回响应的快捷函数, 封装了HttpResponse对象并做了额外处理
# 主要用于向浏览器返回渲染的模板文件
def index(request):
    return render(request, 'index.html', {})


class Person:

    def __init__(self):
        self.sex = "女"


# 不能传参
def func1():
    return "今天不努力, 就...."


# def index1(request):
#     # 键: 模板中的变量名.
#     # 值: 字符串, 整数, 列表, 字典, 对象, 函数
#     dic = {
#         "name": "赵灵银",
#         "age": 20,
#         "hobby": ["演戏", "唱歌"],
#         "description": {"job": "演员", "face": "美女"},
#         "person": Person(),
#         "func": func1
#     }
#
#     return render(request, 'index1.html', dic)


def index1(request):
    name = "ZhaoLiYing"
    age = 20
    hobby = ["演戏", "唱歌"]
    description = {"job": "演员", "face": "美女"}
    person = Person()
    func = func1

    # locals()功能: 收集当前函数中所有的局部变量, 形成字典返回. 键变量名, 值变量值.
    print(locals())

    return render(request, 'index1.html', locals())
