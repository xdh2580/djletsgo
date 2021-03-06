"""djletsgo URL Configuration

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
from dj import views
from dj.dbopt import insert, get, update, delete
from dj.mine import form
urlpatterns = [
    path('index', views.index),
    path('test/', views.test),
    path('admin/', admin.site.urls),
    path('dbinsert/', insert.insert),
    path('dbget/', get.get),
    path('dbmod/', update.update),
    path('dbdel/', delete.delete),
    path('form/', form.search_form),
    path('search/', form.search),
    path('search_post/', form.search_post)
]
