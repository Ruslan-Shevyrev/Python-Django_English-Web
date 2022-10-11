from django.db import models
from ckeditor.fields import RichTextField


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = RichTextField(blank=True, null=True)
    #full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Посты'
        verbose_name_plural = 'Посты'
