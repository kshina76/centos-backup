from django.shortcuts import render
from django.views.generic import TemplateView, FormView

from .forms import UserForm

# Create your views here.

'''
# 関数ベースでviewを実装した場合。基本的に関数ベースでは実装しない。後述するクラスベースで行わないと、データベースをrenderに渡せない。
# https://e-tec-memo.herokuapp.com/article/70/
def form_view(request):
    template_name = 'form.html'
    return render(request, template_name)
'''

'''
今回は、TemplateViewでフォームを実装したが、実際には、GETはTemplateViewで書いて、POSTはFormViewで書くということが多いらしい
https://hombre-nuevo.com/python/python0056/
https://qiita.com/ytyng/items/7cb3c3a5605974151678

よく使うview
https://btj0.com/blog/django/method-attribute/

わかったことは、djangoでは色々なviewが用意されていて、用途に応じたviewを継承することで実装するということ。
そして、様々なviewは全てgeneric.base.Viewというクラスを継承しているので、どのviewにもpostやgetがあるのはこれが理由だと思う。
'''


# TemplateViewでもできるけど、ベストプラクティスではない（後述のFormViewを使うべきだと思う）
'''
class FormViewer(TemplateView):
    template_name = 'form.html'
    
    # urlにアクセスされた際に、一番最初に読み込まれるページを作成。UserForm()によって入力欄を作成している
    # def get(self, request, *args, **kargs):
    #     context = super().get_context_data(**kargs)
    #     context['form'] = UserForm()
    #     return render(request, self.template_name, context)
    
    
    # getメソッドはTemplateViewで実装されていて、ただ単にget_context_dataメソッドを呼び出して、render_to_responseで返しているだけ。
    # なので、getメソッドをオーバーライドするのではなくて、get_context_dataをオーバーライドすればいい。
    # renderを使わないので、request引数が無いように見えるが、render_to_responseの返り値に元からrequestが入っているので問題ない。
    def get_context_data(self, **kargs):
        context = super().get_context_data(**kargs)
        context['form'] = UserForm()
        return context

    # formに入力してsubmit(POST)された際に実行されるメソッド
    # TemplateViewのpostメソッドをオーバーライドしている
    # POSTで条件分岐をさせるやり方は、関数ベースだけなので、クラスベースではFormViewを使って条件分岐なしで書いたほうがいい。（後述）
    def post(self, request, *args, **kargs):
        context = super().get_context_data(**kargs)
        if request.method == 'POST':
            form = UserForm(request.POST)
            context['name'] = request.POST['name']
            context['email'] = request.POST['email']
            context['form'] = form
        else:
            context['form'] = UserForm() 
        return render(request, self.template_name, context)
'''
class FormViewer(FormView):
    # template_nameはクラス変数なので、ここでhtmlを指定しておけば、getされた時に勝手にrender_to_responseが呼ばれて、レンダリングされる。
    # でも、可読性の部分でそれはどうなのかな？？
    template_name = 'form.html'
    form_class = UserForm

    '''
    # get_context_dataは、python側からhtmlに埋め込みたい変数がないなら使わなくていい。
    # つまり、ここがなくてもフォームは表示される。データベースからデータを取ってきて埋め込みたいなら必要。
    # getは、内部でrender_to_responseが呼ばれているから問題ない。
    def get_context_data(self, **kargs):
        context = super().get_context_data(**kargs)
        context['form'] = UserForm()
        return context
    '''

    # リクエストがPOSTだった場合に呼ばれる。GETの場合は呼ばれない。
    # 今回はmailを実際に送らないので、renderをreturnしているが、mailを送りたいなら以下を参考にする
    # https://codor.co.jp/django/how-to-make-contact-form
    def form_valid(self, form):
        context = super().get_context_data()
        form = UserForm(self.request.POST)
        context['name'] = self.request.POST['name']
        context['email'] = self.request.POST['email']
        context['form'] = form
        return render(self.request, self.template_name, context)