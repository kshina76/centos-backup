from django.urls import path
from . import views

# int:pkはurlに指定された値をそのままviewに流す役割がある。つまり、pkという値がviewで有効になる。
# 例えば、post/1/にアクセスされたらpkに1が代入されて、viewに渡されるというイメージ
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # crudのr(read)
    path('post/new/', views.post_new, name='post_new'),  # crudのc(create)
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),  # crudのu(update)
]