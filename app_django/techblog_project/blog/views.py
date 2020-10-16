from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from blog.models import Post

# 全体を表示するためのview
class IndexView(generic.ListView):
    model = Post # def_querysetをオーバーライドしているからあってもなくても変わらない
    template_name = 'blog/post_list.html'
    context_object_name = 'latest_blog_list'
    """
    model=Postをここに定義するなら、get_querysetをオーバーライドする必要はないが、
    「最新の5件だけを表示」といったカスタマイズをしたいなら、model=Postを定義しないで、
    get_querysetを定義する必要がある。
    """
    
    """
    最新の5件を取得してhtml内のlatest_blog_listに格納する
    lteはless than qualの略で、現在時間より過去のものを古い順に格納する
    
    to do. recentlyの記事を実装するには逆方向からfor文で回す必要がある
    """
    def get_queryset(self):
        return Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')[:5]


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

