from django.urls import path
from . import views



urlpatterns = [
    path('', views.home_page, name='home'),
    path('category/<int:pk>/', views.category_page, name='category'),
    path('news/<int:pk>/', views.news_page, name='news_page'),
    path('news/<int:pk>/add_favorite/', views.add_favorite, name='add_favorite'),
    path('news/<int:pk>/remove_favorite/', views.remove_favorite, name='remove_favorite'),
    path('favorites/', views.favorites_page, name='favorites_list'),
    path('register', views.Register.as_view()),
    path('logout', views.logout_view)

]
