from django.urls import path
from api.views import Home

from . import views

app_name = 'api'
urlpatterns = [
    path('', Home.as_view(), name='home'),
]
