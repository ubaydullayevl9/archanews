from django.urls import path
from . import views



urlpatterns = [
    path('', views.home_page),
    path('category/<int:pk>', views.category_page),
    path('news/<int:pk>', views.news_page),
    path('news/<int:pk>/add_favorite/', views.add_favorite, name='add_favorite'),
    path('news/<int:pk>/remove_favorite/', views.remove_favorite, name='remove_favorite'),
    path('favorites/', views.favorites_list, name='favorites_list'),
]