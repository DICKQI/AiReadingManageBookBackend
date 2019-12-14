from django.db import models
from django.utils.timezone import now


class Password(models.Model):
    """密码"""
    password = models.CharField(verbose_name='密码', default=None, blank=False, max_length=100)


class Administrator(models.Model):
    """总教师/管理员"""
    genderChoice = (
        ('male', '男'),
        ('female', '女')
    )

    userRoles = (
        ('administrator', '管理员'),
        ('teacher', '教师')
    )

    idCard = models.BigIntegerField(verbose_name='证件号', default=0, primary_key=True, blank=False)

    password = models.ForeignKey(Password, verbose_name='账户密码', on_delete=models.CASCADE, default=None, blank=False)

    name = models.CharField(verbose_name='姓名', max_length=50, default=None, blank=False)

    gender = models.CharField(verbose_name='性别', choices=genderChoice, default='male', blank=False, max_length=20)

    role = models.CharField(verbose_name='用户身份', choices=userRoles, default='administrator', blank=False, max_length=20)

    last_login_time = models.DateTimeField(verbose_name='最后登录时间', default=now, blank=False)

    is_cancel = models.BooleanField(verbose_name='是否注销', default=False)

    class Meta:
        verbose_name = '管理员'
        verbose_name_plural = verbose_name + '列表'
        db_table = 'Administrator'

    def __str__(self):
        return self.name
