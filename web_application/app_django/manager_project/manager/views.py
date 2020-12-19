from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
from django.views.generic import TemplateView

from manager.models import *

# htmlとデータベースのデータを混ぜて返す
# contextの辞書型にデータを随時追加していき、最後にrenderでhtmlと混ぜるという動作
class WorkerListView(TemplateView):
    template_name = "worker_list.html"

    def get(self, request, *args, **kwargs):
        # python2の書き方 context = super(WorkerListView, self).get_context_data(**kwargs)
        # pythonのsuperの仕様として、 super(hikisu1, hikisu2)とあったら、hikisu1のsuper。つまり、hikisu1の親クラスを参照してくださいということ。
        # しかし、python3からは、自クラスの親クラスを参照したいときは、引数は省略できる。
        # https://www.codeflow.site/ja/article/python-super
        # get_context_dataは辞書型のデータを返してくるので、そこにいろいろ追加していくイメージ(後述する例では、workersというところにデータベースのデータを入れている)
        context = super().get_context_data(**kwargs)

        # context['workers']によって、htmlファイル内でworkersという変数が有効になる
        workers = Worker.objects.all()
        context['workers'] = workers

        # render(request, htmlファイルの情報, データベース内にあるデータ)
        # 似たメソッドにrender_to_responseやHttpResponseなどがあるが、低水準だったり非推奨なので、renderを使っておけばいい
        # https://nihaoshijie.hatenadiary.jp/entry/2015/08/30/174206        
        return render(self.request, self.template_name, context)