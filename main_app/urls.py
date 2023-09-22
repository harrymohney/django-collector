from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
]


# from django.contrib import admin
# from django.urls import path
# from main_app import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.home, name='home'),
#     path('about/', views.about, name='about'),
#     path('all_finches/', views.all_finches, name='all_finches')
# ]