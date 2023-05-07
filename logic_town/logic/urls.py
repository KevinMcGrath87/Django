from django.urls import path
from .import views

urlpatterns =[
    path('',views.implication),
    path('root', views.root),
    path('blog', views.blog),
    path('blog/<str:name>', views.blog),
    path('blog/new', views.new_blog),
    path('blog/create',views.create),
    path('blog/<int:number>',views.number),
    path('blog/<int:number>/edit',views.edit),
    path('json',views.json_response),
    path('form', views.form),
    path('counter',views.counter),
    path('counter_display',views.counter_display),
]