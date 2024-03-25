# myapp/urls.py
from django.urls import path
from .views import signup_view, login_view,signup

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('signup2/', signup, name='signup2'),
]
