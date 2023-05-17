from django.urls import path

from .views import (
    homePage_View,
    CreateUser_View,
    delete_todo_view
)



urlpatterns = [
    path('', homePage_View, name='home'),
    path('signup/', CreateUser_View.as_view(), name='signup'),
    path('<int:id>/', delete_todo_view, name='delete')
]