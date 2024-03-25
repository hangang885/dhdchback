from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import serializers

from django.contrib.auth import get_user_model


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'name', 'phone_number')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            name=validated_data['name'],
            phone_number=validated_data['phone_number']
        )
        return user


class SignUpSerializer(serializers.ModelSerializer):
    # 비밀번호는 write_only 옵션을 True로 설정하여, 응답에 포함되지 않도록 합니다.
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        # 사용자 모델의 create_user 메소드를 사용하여 비밀번호 해싱과 함께 사용자를 생성합니다.
        return User.objects.create_user(**validated_data)



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            raise serializers.ValidationError("유효하지 않은 로그인 정보입니다.")
        data['user'] = user
        return data
