from django.urls import path

from . import views

# pollsアプリのurlファイルと認識させるために、名前空間の設定をする（大規模な開発になってくると必要になる）
app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]