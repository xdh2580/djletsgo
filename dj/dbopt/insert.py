import random

from django.http import HttpResponse

from dj.models import DjTest1


# 数据库操作之插入数据
def insert(request):
    r = str(random.random())
    test1 = DjTest1(name=r)
    test1.save()
    return HttpResponse("<p>数据添加成功！"+r+"</p>")

