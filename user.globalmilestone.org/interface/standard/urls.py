from django.urls import path
from standard import views

urlpatterns = [
	path('', views.standard, name='standard'),
]
