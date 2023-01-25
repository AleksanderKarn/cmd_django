from django.db import models
import datetime

from django.urls import reverse
from pytils.translit import slugify


NULLABLE = {'blank': True, 'null': True}

class Post(models.Model):
    '''Данные о посте'''
    tittle = models.CharField("Заголовок", max_length=100)
    slug = models.SlugField("slug", max_length=250,  db_index=True)
    content = models.TextField("Содержимое" )
    img = models.ImageField("Превью", upload_to='image/%Y', **NULLABLE)
    date_create = models.DateField("Дата создания", auto_now=datetime)
    publication = models.BooleanField("Признак публикации", default=False)
    view_count = models.IntegerField("Счетчик просмотров", default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.tittle)

        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})


    def __str__(self):
        return f'{self.tittle}, {self.date_create}'


    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
