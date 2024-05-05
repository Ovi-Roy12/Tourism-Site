from django.urls import path
from .import views

app_name = "App_Content"

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('my_booking/', views.My_Booking, name='my_booking'),
    path('view_details/<int:destination_id>/', views.view_details, name='view_details'),
    path('search_results/', views.search_results, name='search_results'),

]
