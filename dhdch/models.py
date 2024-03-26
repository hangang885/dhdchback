from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'user'  # 실제 데이터베이스의 테이블 이름을 지정
