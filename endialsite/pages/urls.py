from django.urls import path, include

from .views import *
from pages import views


urlpatterns = [
    # path('', views.index , name = "index"),
    #     path('d/<str:url>/', PostDetailView.as_view(), name='detail'),
    #     path('register/', register, name="register"),
    #
    #     path('accounts/', include('django.contrib.auth.urls')),
]
