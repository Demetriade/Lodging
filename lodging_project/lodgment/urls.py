from django.urls import path
from .views import LodgeListView, LodgeDetailView, LodgeCreateView, LodgeUpdateView, LodgeDeleteView
from . import views

urlpatterns = [
    path('', LodgeListView.as_view(), name='lodgment-home'),
    path('lodge/<int:pk>/', LodgeDetailView.as_view(), name='lodge-detail'),
    path('lodge/new/', LodgeCreateView.as_view(), name='lodge-create'),
    path('lodge/<int:pk>/update/', LodgeUpdateView.as_view(), name='lodge-update'),
    path('lodge/<int:pk>/delete/', LodgeDeleteView.as_view(), name='lodge-delete'),
]