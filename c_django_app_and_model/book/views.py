from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import Author  # 当前应用的Models


# Create your views here.

# /book/goods
def goods(request):
    return HttpResponse("book的goods")


# /book/author/
class AuthorView(View):

    # 处理get请求
    def get(self, request):
        return render(request, "author.html")

    # 处理post请求
    def post(self, request):
        # 获取前端数据
        name = request.POST.get("user", "")
        gender = request.POST.get("sex", "")
        phone = request.POST.get("phone", "")
        email = request.POST.get("email", "")
        comment = request.POST.get("con", "")

        # 方法一: 通过objects对象提供的统一函数插入数据
        # try:
        #     Author.objects.create(name=name,
        #                           gender=gender,
        #                           phone=phone,
        #                           email=email,
        #                           comment=comment)
        # except Exception as e:
        #     print(e)
        #     return HttpResponse("添加失败！")

        # 方法二: 通过模型类，进行属性赋值，保存
        author = Author(name=name, phone=phone)
        author.gender = gender
        author.email = email
        author.save()  # 保存 -> 插入

        return HttpResponse("添加成功！")


def author_select(request, id):
    # all() -> 查询全部记录, 返回QuerySet查询对象.
    # result = Author.objects.all()
    # print(result)
    # print(result[0].name, result[0].phone, result[0].email)

    # get() -> 返回一条查询结果, 如果结果不存在或者有多个则抛出异常; pk表示一个表的主键.
    # result = Author.objects.get(pk=id)
    # print(result)

    # filter() -> 根据条件过滤, 查询符合条件的多条记录, 返回queryset.
    # result = Author.objects.filter(gender="0")
    # print(result)

    # exclude() -> 根据条件过滤, 查询符合条件之外的全部记录, 返回不符合的queryset.
    # result = Author.objects.exclude(gender="0")
    # print(result)

    # 按照列查询, 返回字典.
    # [{'name': 'brian', 'phone': '123456'}, {'name': 'lulu', 'phone': '124567'}, {'name': '莫言', 'phone': '1245673'}]
    # result = Author.objects.values("name", "phone")
    # print(result)

    # [('brian', '123456'), ('lulu', '124567'), ('莫言', '1245673')]
    # result = Author.objects.values_list("name", "phone")
    # print(result)

    # 默认是按照升序排序, 降序排序则需要在列前增加'-'表示
    # result = Author.objects.order_by("-id")
    # print(result)

    # queryset对象支持链式写法: 函数返回值是queryset对象就可以"."继续调用.
    result = Author.objects.filter(gender='1').values("name")
    print(result)

    result = Author.objects.filter(gender='1').count()
    print(result)

    result = Author.objects.filter(gender='1').exists()
    print(result)

    return HttpResponse("查询成功")


# 修改操作: /book/author/update/?name=Brian&phone=1234567
def author_update(request):
    name = request.GET.get("name")
    phone = request.GET.get("phone")

    # 方法1: 找记录 -> 修改属性 -> 保存信息
    # author = Author.objects.get(pk=1)
    # author.name = name
    # author.phone = phone
    # author.save()

    # 方法2: 批量修改, 查询结果queryset -> update函数一起修改.
    result = Author.objects.filter(gender='0')
    result.update(comment='无内容')

    return HttpResponse("修改成功")


# 删除操作: /book/author/delete/
def author_delete(request):
    # 删除一条记录
    # author = Author.objects.get(pk=1)
    # author.delete()

    # 删除多条记录 queryset
    result = Author.objects.filter(gender='0')
    result.delete()

    return HttpResponse("删除成功")
