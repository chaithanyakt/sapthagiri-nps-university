from django.contrib import admin
from django.urls import path, include
from accounts.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('accounts.urls')),
    path('students/', include('students.urls')),
    path('teachers/', include('teachers.urls')),
    path('dashboard/', dashboard, name='dashboard'),
]