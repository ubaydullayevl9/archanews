from django.shortcuts import render
from .models import NewsCategory, News
from .models import Favorite
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required
def add_favorite(request, pk):
    news = News.objects.get(id=pk)
    Favorite.objects.get_or_create(user=request.user, news=news)
    return redirect('news_page', pk=pk)

@login_required
def remove_favorite(request, pk):
    news = News.objects.get(id=pk)
    Favorite.objects.filter(user=request.user, news=news).delete()
    return redirect('news_page', pk=pk)

@login_required
def favorites_list(request):
    favorites = News.objects.filter(favorite__user=request.user)
    return render(request, 'favorites.html', {'favorites': favorites})

# Create your views here.
def home_page(request):
    news = News.objects.all()
    categories = NewsCategory.objects.all()


    context = {
        'news': news,
        'categories': categories
    }
    return render(request, 'home.html', context)


def category_page(request, pk):
    category = NewsCategory.objects.get(id=pk)
    news = News.objects.filter(news_category=category)


    context = {
        'category': category,
        'news': news
    }
    return render(request, 'category.html', context)



def news_page(request, pk):
    news = News.objects.get(id=pk)
    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(news=news, user=request.user).exists()

    context = {
        'news': news,
        'is_favorite': is_favorite
    }
    return render(request, 'news.html', context)


@login_required
def add_to_favorites(request, pk):
    news = News.objects.get(id=pk)
    Favorite.objects.get_or_create(user=request.user, news=news)
    return redirect(f'/news/{pk}')

