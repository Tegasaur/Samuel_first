from django.contrib import admin
from django.urls import path
from app1 import views
app_name='app1'

urlpatterns = [
    path('',views.index,name="index"),
    path('purchase/',views.access,name="purchase"),
    path('admin/', admin.site.urls),
]
