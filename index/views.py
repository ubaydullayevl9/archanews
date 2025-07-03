from django.shortcuts import render, get_object_or_404, redirect
from .models import NewsCategory, News, Favorite
from django.contrib.auth.decorators import login_required

# Главная страница
def home_page(request):
    news = News.objects.all()
    categories = NewsCategory.objects.all()

    context = {
        'news': news,
        'categories': categories
    }
    return render(request, 'home.html', context)

# Страница категории
def category_page(request, pk):
    category = NewsCategory.objects.get(id=pk)
    news = News.objects.filter(news_category=category)

    context = {
        'category': category,
        'news': news
    }
    return render(request, 'category.html', context)

# Страница отдельной новости
def news_page(request, pk):
    news = News.objects.get(id=pk)

    # Проверка, добавлено ли в избранное
    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = news.favorite_set.filter(user=request.user).exists()

    context = {
        'news': news,
        'is_favorite': is_favorite
    }
    return render(request, 'news.html', context)

# Добавить новость в избранное
@login_required
def add_favorite(request, pk):
    news = get_object_or_404(News, pk=pk)
    Favorite.objects.get_or_create(user=request.user, news=news)
    return redirect('news_page', pk=pk)

# Удалить из избранного
@login_required
def remove_favorite(request, pk):
    news = get_object_or_404(News, pk=pk)
    Favorite.objects.filter(user=request.user, news=news).delete()
    return redirect('news_page', pk=pk)

# Страница избранного
@login_required
def favorites_page(request):
    favorites = Favorite.objects.filter(user=request.user)
    context = {'favorites': favorites}
    return render(request, 'favorites.html', context)