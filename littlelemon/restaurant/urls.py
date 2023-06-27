from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path('reservations/', views.reservations, name="reservations"),
    path("menu/", views.MenuItemView.as_view(), name="api_menu"),
    path("menu/<int:pk>", views.SingleMenuItemView.as_view()),
]
