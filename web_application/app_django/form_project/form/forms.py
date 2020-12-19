from django import forms

# formをdjangoで作る理由としては、評価が簡単という理由がある
# https://blog.mtb-production.info/entry/2018/12/20/201057
class UserForm(forms.Form):
    name = forms.CharField(label='名前', max_length=100)
    email = forms.EmailField(label='メール', max_length=100)