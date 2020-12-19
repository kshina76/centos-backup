from django.urls import path

from . import views

# pollsアプリのurlファイルと認識させるために、名前空間の設定をする（大規模な開発になってくると必要になる）
app_name = 'polls'


"""
クラスベースの場合のurlconfの書き方
"""
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

"""
関数ベースの場合のurlconfの書き方

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
"""