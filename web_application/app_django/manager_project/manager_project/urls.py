"""manager_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path

import manager.views as manager_view


urlpatterns = [
    # フルパスで指定する方法
    # path('admin/', admin.site.urls),
    # path('worker_list/', manager_view.WorkerListView.as_view())  # URLとViewを組み合わせる！
    
    # 正規表現でパスを指定する方法
    # re_path(ブラウザで指定するurl, リダイレクト先)　という構文になっている。
    # http://127.0.0.1:8000/worker_list/ をブラウザで開くと、自分で作成したページが表示される
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^worker_list/', manager_view.WorkerListView.as_view())  # URLとViewを組み合わせる！
]
