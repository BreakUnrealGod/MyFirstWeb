from django.db import models

# Create your models here.
from user.models import User


class Book(models.Model):
    bookauthor = models.CharField(max_length=20, verbose_name='作者', default='神秘作家')
    bookcontent = models.TextField(verbose_name='内容', default="神秘内容")
    bookcover = models.ImageField(upload_to='books/')
    bookname = models.CharField(max_length=20, verbose_name='书名', default='神秘书籍')
    is_collection = models.BooleanField(default=False)
    is_buy = models.BooleanField(default=False)


    #外键关系:一对多
    # bookname = models.ForeignKey(to=User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.bookcover

    class Meta:
        db_table = 'book'
        verbose_name = '书'
        verbose_name_plural = verbose_name