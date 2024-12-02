from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='sarcopenia-index'),
    path('sarcopenia/diagnosis/<int:data_id>/', views.diagnosis, name='diagnosis'),
    path('sarcopenia/model_two/<int:data_id>/', views.model_two, name='model_two'),
    path('sarcopenia/model_three/<int:model_two_id>/', views.model_three, name='model_three'),
]


