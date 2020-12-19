from django.db import models
from django.conf import settings
from django.utils import timezone
from markdownx.models import MarkdownxField

from django.utils.safestring import mark_safe
from markdownx.utils import markdownify

class Post(models.Model):
    title = models.CharField(max_length=100)
    ## text = models.TextField()
    text = MarkdownxField('本文', help_text='Markdown形式で書いてください。')
    created_date = models.DateTimeField(default=timezone.now)

    ## markdownで記事を書くための自作メソッド
    ## これによってmarkdownを解析してhtmlに変換？して返してくれる
    def get_text_markdownx(self):
        return mark_safe(markdownify(self.text))

    ## 年月日だけにして返す
    def split_date(self):
        created_date_str = self.created_date.strftime('%Y-%m-%d %H:%M:%S')
        return created_date_str.split()[0]

    def __str__(self):
        return self.title