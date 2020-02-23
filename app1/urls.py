from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nat_gam/',views.nat_gam),
    path('nat_flo/',views.nat_flo),
    path('nat_ani/',views.nat_ani),
]