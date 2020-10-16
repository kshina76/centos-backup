
from django.urls import path
from . import views

# これによって、他のところからurlconfigにアクセスする際にはblog:post_detailのようにblogを付けなければいけない
app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='post_detail'),
]