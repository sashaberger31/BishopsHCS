from django.urls import path
from pages import views

urlpatterns = [
	path('us/', views.us, name = 'en'),
	path('mx/', views.mx, name = 'mx'),
	path('cn/', views.cn, name = 'cn'),
	path('us/enroll/', views.enroll_us, name = 'enroll_us'),
	path('us/about/', views.about_us, name = 'about_us'),
	path('us/tutor/', views.tutor_us, name = 'tutor_us'),
	path('', views.fallback, name = 'fallback')
]
