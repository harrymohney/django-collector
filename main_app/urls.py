from django.urls import path
from . import views
from main_app.views import FinchCreate

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('finches/', views.finches_index, name='index'),
  path('finches/<int:finch_id>/', views.finch_detail, name='finches_detail'),
  path('finches/create/', FinchCreate.as_view(), name='finches_create')
]