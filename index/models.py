from django.db import models


# Create your models here.
class NewsCategory(models.Model):
    class Meta:
        verbose_name_plural = 'Категории новостей'
    category_name = models.CharField(max_length= 16)
    added_date = models.DateTimeField(auto_now_add =True)


    def __str__(self):
        return str(self.category_name)


class News(models.Model):
    class Meta:
        verbose_name_plural = 'Новости'
    name = models.CharField(max_length=128)
    text = models.TextField()
    news_photo = models.ImageField(upload_to='media', null=True, blank=True)
    news_category = models.ForeignKey(NewsCategory,
                                 on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

from django.contrib.auth.models import User

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'news')
        # Чтобы один пользователь не мог добавить одну и ту же новость дважды