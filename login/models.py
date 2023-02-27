from django.db import models


# Create your models here.
class User(models.Model):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    name = models.CharField(max_length=128, unique=True, verbose_name="用户名")
    password = models.CharField(max_length=256, verbose_name="密码")
    email = models.EmailField(unique=True, verbose_name="电子邮箱")
    sex = models.CharField(max_length=32, choices=gender, default="男", verbose_name="性别")
    c_time = models.DateTimeField(auto_now_add=True)
    has_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]  # 按'c_time'降序排序
        verbose_name = "用户"  # 为模型对象创建一个更方便识别的名称
        verbose_name_plural = "用户"  # verbose_name的复数形式


class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ":  " + self.code

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码"