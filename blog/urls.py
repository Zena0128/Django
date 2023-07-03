from django.urls import path
from . import views
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', BlogList.as_view()),
    path('<int:pk>/', BlogDetail.as_view()),
]