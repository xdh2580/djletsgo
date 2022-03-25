from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("cool")


def test(request):
    a = '666'
    return render(request, 'test.html', {'a': a})
