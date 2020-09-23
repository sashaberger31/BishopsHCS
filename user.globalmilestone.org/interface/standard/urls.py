from django.urls import path, include
from standard import views


urlpatterns = [
	path('accounts/', include('django.contrib.auth.urls')),
]
