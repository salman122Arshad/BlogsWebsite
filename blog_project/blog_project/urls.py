from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('login'), name='home'),  # Redirect root to login
    path('blog/', include('blog.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Authentication URLs
]
