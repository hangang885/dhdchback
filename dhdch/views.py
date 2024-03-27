from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import login
from .serializers import LoginSerializer
# from .serializers import SignUpSerializer, LoginSerializer
from drf_yasg.utils import swagger_auto_schema
# from .serializers import UserSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer,RefreshToken
import jwt

#
# @swagger_auto_schema(method="post", request_body=UserSerializer)
# @api_view(['POST'])
# def signup(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"message": "회원가입이 성공적으로 완료되었습니다."}, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @swagger_auto_schema(methods=['post'], request_body=SignUpSerializer)
# @api_view(['POST'])
# def signup_view(request):
#     # 요청으로부터 받은 데이터로 시리얼라이저 인스턴스를 생성합니다.
#     serializer = SignUpSerializer(data=request.data)
#     # 시리얼라이저의 유효성 검사를 수행합니다.
#     if serializer.is_valid():
#         # 유효성 검사를 통과한 경우, 사용자를 생성합니다.
#         serializer.save()
#         # 사용자 생성 성공 응답을 반환합니다.
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     else:
#         # 유효성 검사를 통과하지 못한 경우, 에러 응답을 반환합니다.
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method="post", request_body=LoginSerializer,)
@api_view(['POST'])
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data.get('user')

        # TokenObtainPairSerializer 대신 직접 토큰 생성
        refresh = RefreshToken.for_user(user)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        return Response(data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)