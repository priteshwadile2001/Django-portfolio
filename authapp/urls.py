from django.contrib import admin 
from django.urls import path,include
from authapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/signup/', views.signup,name='signup'),
    path('auth/login/', views.handleLogin,name='login'),
    path('auth/logout/', views.handleLogout,name='logout'),
]