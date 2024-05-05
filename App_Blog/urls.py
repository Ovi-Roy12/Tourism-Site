from django.urls import path
from .views import blog_list, blog_detail

app_name = 'App_Blog'

urlpatterns = [
    path('blog/', blog_list, name='blog_list'),
    path('blog/<int:blog_id>/', blog_detail, name='blog_detail'),
]

