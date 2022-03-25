from django.http import HttpResponse

from dj.models import DjTest1


# 数据库操作
def update(request):
    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    test1 = DjTest1.objects.get(id=1)
    test1.name = 'Google'
    test1.save()

    # 另外一种方式
    # Test.objects.filter(id=1).update(name='Google')

    # 修改所有的列
    # Test.objects.all().update(name='Google')

    return HttpResponse("<p>修改成功</p>")
