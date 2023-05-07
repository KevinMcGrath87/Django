from . import views
from django.urls import path


urlpatterns=[
    path('display_time',views.display_time),
]