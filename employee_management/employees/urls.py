from django.urls import path
from .views import register, user_login, user_logout, employee_list
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('list/', employee_list, name='employee_list'),
]
