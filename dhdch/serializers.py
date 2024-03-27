from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import serializers

from django.contrib.auth import get_user_model

import hashlib
import base64
from .models import User
#
# User = get_user_model()
#
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('email', 'password', 'name', 'phone')
#         extra_kwargs = {'password': {'write_only': True}}
#
#     def create(self, validated_data):
#         user = User.objects.create_user(
#             email=validated_data['email'],
#             password=validated_data['password'],
#             name=validated_data['name'],
#             phone=validated_data['phone']
#         )
#         return user
#
#
# class SignUpSerializer(serializers.ModelSerializer):
#     # 비밀번호는 write_only 옵션을 True로 설정하여, 응답에 포함되지 않도록 합니다.
#     password = serializers.CharField(write_only=True)
#
#     class Meta:
#         model = User
#         fields = ['email', 'password']
#
#     def create(self, validated_data):
#         # 사용자 모델의 create_user 메소드를 사용하여 비밀번호 해싱과 함께 사용자를 생성합니다.
#         return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = self.validate_user_credentials(data['email'], data['password'])
        if not user:
            raise serializers.ValidationError("유효하지 않은 로그인 정보입니다.")
        # 로그인 성공 시, 사용자 객체를 `validated_data`에 추가
        data['user'] = user
        return data

    def validate_user_credentials(self, email, password):
        """
        사용자의 이메일과 비밀번호를 검증하는 메서드.
        비밀번호는 데이터베이스에 저장된 형식과 동일하게 암호화하여 비교합니다.
        """
        try:
            user = User.objects.get(email=email)
            # encrypted_password = self.encrypt_password(password)
            if user.password == password:
                return user
        except User.DoesNotExist:
            return None

    def encrypt_password(self, password):
        """
        비밀번호를 암호화하는 메서드.
        """
        password_base64 = base64.b64encode(password.encode('utf-8')).decode('utf-8')
        md5_hash = hashlib.md5(password_base64.encode('utf-8')).hexdigest().upper()
        sha512_hash = hashlib.sha512(md5_hash.encode('utf-8')).hexdigest().upper()
        return sha512_hash