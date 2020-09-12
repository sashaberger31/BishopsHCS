from django.urls import path
from pages import views

urlpatterns = [
	path('us/', views.HomeView.as_view(locale = "us"), name = 'en'),
	path('mx/', views.HomeView.as_view(locale = "mx"), name = 'mx'),
	path('cn/', views.HomeView.as_view(locale = "cn"), name = 'cn'),
	path('us/enroll/', views.EnrollView.as_view(locale = "us"), name = 'enroll_us'),
	path('mx/enroll/', views.EnrollView.as_view(locale = "mx"), name = 'enroll_mx'),
	path('cn/enroll/', views.EnrollView.as_view(locale = "cn"), name = 'enroll_cn'),
	path('us/about/', views.AboutView.as_view(locale = "us"), name = 'about_us'),
	path('mx/about/', views.AboutView.as_view(locale = "mx"), name = 'about_mx'),
	path('cn/about/', views.AboutView.as_view(locale = "cn"), name = 'about_cn'),
	path('us/tutor/', views.tutor_us, name = 'tutor_us'),
	path('', views.fallback, name = 'fallback')
]
