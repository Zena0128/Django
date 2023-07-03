from django.urls import path
from . import views
from .views import login, signup, logout

app_name = 'accounts'

urlpatterns = [
    path('login/', login),
    path('signup/', signup),
    path('logout/', logout)
]