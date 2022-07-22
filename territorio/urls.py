from django.urls import path
from . import views                 #El punto significa que, desde dentro de la carpeta

app_name = "territorio"
urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('saludar/', views.saludo, name="saludar"),
    path('saludo/<str:dato>', views.saludoEspecial, name="saludo"),
    path('calcula/<int:ope>/<int:num1>/<int:num2>', views.calculadora, name="calcula"),
    path('loginForm/', views.loginForm, name="login-form"),
    path('login/', views.login, name="login"),
]