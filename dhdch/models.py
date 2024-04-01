import base64
import hashlib

from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('이메일은 필수입니다.')

        # 이메일 중복 검사
        if self.model.objects.filter(email=self.normalize_email(email)).exists():
            raise ValidationError('이미 사용 중인 이메일입니다.')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = encrypt_password(password)  # 비밀번호 암호화
        user.save(using=self._db)
        return user

def encrypt_password(password):
    """
    비밀번호를 암호화하는 메서드.
    """
    password_base64 = base64.b64encode(password.encode('utf-8')).decode('utf-8')
    md5_hash = hashlib.md5(password_base64.encode('utf-8')).hexdigest().upper()
    sha512_hash = hashlib.sha512(md5_hash.encode('utf-8')).hexdigest().upper()
    return sha512_hash

class User(models.Model):
    objects = UserManager()  # UserManager 사용

    name = models.CharField(max_length=20)
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="전화번호 형식이 유효하지 않습니다.")]
    )
    address = models.CharField(max_length=100, blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True)  # 이메일은 고유해야 합니다.
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'user'
