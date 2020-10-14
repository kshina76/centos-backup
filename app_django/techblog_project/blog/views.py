from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from blog.models import Post

# 全体を表示するためのview
class IndexView(generic.ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'latest_blog_list'

    # 最新の5件を取得する
    # lteはless than qualの略で、現在時間より過去のものを古い順に格納する
    # to do. なので、recentlyの記事を実装するには逆方向からfor文で回す必要がある
    def get_queryset(self):
        return Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')[:5] 