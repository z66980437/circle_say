from django.urls import path

from scenic import views

urlpatterns = [
    path('scenics/', views.ScenicView.as_view(), name='scenics'),
    path('scenics/<int:pk>/', views.ScenicDetailView.as_view(), name='scenic'),
]