from django.urls import path
from . import views
from main_app.views import FinchCreate
from main_app.views import FinchUpdate
from main_app.views import FinchDelete

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('finches/', views.finches_index, name='index'),
  path('finches/<int:finch_id>/', views.finch_detail, name='finches_detail'),
  path('finches/create/', FinchCreate.as_view(), name='finches_create'),
  path('finches/<int:pk>/update/', FinchUpdate.as_view(), name='finches_update'),
  path('finches/<int:pk>/delete/', FinchDelete.as_view(), name='finches_delete')

]