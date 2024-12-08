from django.db import models


# Create your models here.

# 类 -> 表; 类变量 -> 字段; 默认表名: 应用名_类名小写
# 书表
class Book(models.Model):
    # !!!如果不写主键, 会自动添加一个整型自增主键.

    # 约束: Field.null, 如果是True, 数据库中存储空值为NULL, 默认为False.
    #      default: 默认值; primary_key: 主键; db_index: 索引设置; unique: 唯一索引

    # 书名 CharField(max_length=None, **options) == char / varchar;
    # 不可以为空; 设置索引.
    book_name = models.CharField(max_length=30, db_index=True)

    # 价格 DecimalField(max_digits=None, decimal_places=2, **options) == decimal(5, 2)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    # 销量 IntegerField(**options) == int
    # 默认值销量为0
    sales = models.IntegerField(default=0)

    # 销售状态 BooleanField(**options) == boolean bit
    # 默认销售状态为True
    is_launched = models.BooleanField(default=True)

    # 出版时间 DateField(auto_now=False, auto_now_add=False, **options) == Date
    # auto_now: 每次保存对象时, 自动设置该字段为当前时间(update).
    # auto_now_add: 当对象第一次被创建时自动设置当前时间(insert). => default = now()
    created_time = models.DateField(auto_now_add=True)

    # 信息修改时间 DateTimeField(auto_now=False, auto_now_add=False, **options) == Datetime
    updated_time = models.DateTimeField(auto_now=True)

    # 备注 TextField(**options) == text 默认不可以为空
    # null=True: 允许可以为空
    remark = models.TextField(null=True)

    # 通过内部类可以对模型做基本设置
    class Meta:
        db_table = "book"  # 自己设置表名

    def __str__(self):
        return self.book_name


# 签约作家
class Author(models.Model):
    # 枚举选项
    GENEDER_CHOICE = [
        (1, "Man"),
        (2, "Woman")
    ]

    name = models.CharField(max_length=30, unique=True)
    phone = models.CharField(max_length=11, unique=True)

    # 枚举类型
    gender = models.IntegerField(choices=GENEDER_CHOICE)
    email = models.EmailField()
    comment = models.TextField(null=True)

    class Meta:
        db_table = "author"

    # 指定该类的对象显示形式
    def __str__(self):
        return self.name


# 作家表
class Publisher(models.Model):
    # 出版社发行编号, 作为主键
    pid = models.CharField(max_length=20, primary_key=True)

    # 出版社名称, db_column设置表中的名字
    pname = models.CharField(max_length=30, db_column="publisher_name")
    phone = models.CharField(max_length=11)
    email = models.EmailField()

    # 出版社地址
    site = models.TextField(max_length=512)

    class Meta:
        db_table = "publisher"
