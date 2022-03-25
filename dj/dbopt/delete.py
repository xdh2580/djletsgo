from django.http import HttpResponse

from dj.models import DjTest1


# 数据库操作
def delete(request):
    try:
        # 删除id=2的数据
        test1 = DjTest1.objects.get(id=2)
        test1.delete()

        # 另外一种方式
        # Test.objects.filter(id=1).delete()

        # 删除所有数据
        # Test.objects.all().delete()

        return HttpResponse("<p>删除成功</p>")
    except Exception:
        return HttpResponse("出错了！")
