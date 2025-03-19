from django.contrib import admin
from django.urls import path, include
from sales.views import create_sale, get_csrf_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/create_sale/', create_sale, name='create_sale'),
    path('api/csrf_token/', get_csrf_token, name='csrf_token'),
    path('api-auth/', include('rest_framework.urls')),
]