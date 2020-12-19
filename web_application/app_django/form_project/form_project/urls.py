"""form_project URL Configuration

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

# from form.views import form_view  関数ベースでviewを実装
import form.views as form_view

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    
    # 関数ベースで実装した場合の書き方。form_view関数はrenderを返してくる。基本的に関数ベースでは実装しないので、後述のクラスベースのやり方で。
    #re_path(r'^user_form/', form_view)

    # クラスベースで実装した場合のrenderの受け取り方
    re_path(r'^user_form/', form_view.FormViewer.as_view())  # urlとviewを組み合わせる

    # includeを使うと、他のurlsファイルに書かれているurlを連結することができる。
    # 詳しくは、https://e-tec-memo.herokuapp.com/article/70/
    # re_path(r'^user_form/', include('dir.urls.py'))   dirディレクトリのurls.pyに書かれているpathをuser_form/に連結するという意味


]
