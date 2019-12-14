from django.db import models
from django.utils.timezone import now
from app.administrator.models import Administrator


# Create your models here.

class Category(models.Model):
    """分类"""
    name = models.CharField(verbose_name='分类名', default='', blank=False, max_length=100)

    count = models.IntegerField(verbose_name='计数', default=0, blank=False)

    createUser = models.ForeignKey(Administrator, verbose_name='创建人', default=None, blank=False,
                                   on_delete=models.CASCADE)

    class Meta:
        verbose_name = '书本分类'
        verbose_name_plural = verbose_name + '列表'
        db_table = 'book_Category'

    def __str__(self):
        return self.name


class Book(models.Model):
    """书籍"""
    name = models.CharField(verbose_name='图书名', default='', blank=False, max_length=100)

    ISBN = models.CharField(verbose_name='图书isbn码', default=0, blank=False, unique=True, max_length=100)

    content = models.TextField(verbose_name='图书内容', default='')

    view = models.BigIntegerField(verbose_name='阅读量', default=0, blank=False)

    createTime = models.DateTimeField(verbose_name='创建时间', default=now, blank=False)

    lastModTime = models.DateTimeField(verbose_name='最后修改时间', default=now, blank=False)

    category = models.ForeignKey(Category, verbose_name='归属分类', on_delete=models.CASCADE, default=None, blank=False)

    createUser = models.ForeignKey(Administrator, verbose_name='创建人', on_delete=models.CASCADE, default=None,
                                   blank=False)

    class Meta:
        verbose_name = '图书'
        verbose_name_plural = verbose_name + '列表'
        db_table = 'book_Book'
        ordering = ['-createTime']

    def __str__(self):
        return self.name
