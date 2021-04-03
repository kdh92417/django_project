from django.db import models

class Account(models.Model):
    user_name   = models.CharField(max_length=30, verbose_name='유저ID')
    password    = models.CharField(max_length=200, verbose_name='유저PW')
    email       = models.EmailField(max_length=200, verbose_name='유저메일')
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name='가입날짜')
    updated_at  = models.DateTimeField(auto_now=True, verbose_name='마지막수정일')

    def __str__(self):
        return self.user_name

    class Meta:
        db_table            = 'accounts'
        verbose_name        = '유저'
        verbose_name_plural = '유저'
