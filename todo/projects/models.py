from django.db import models
from django.contrib.auth import get_user_model


class Project(models.Model):
    name = models.CharField(max_length=128, verbose_name='name')
    rep_link = models.URLField(verbose_name='repository')
    users = models.ManyToManyField(get_user_model())

    def __str__(self):
        return f'{self.name}'


class ToDo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='project')
    text = models.TextField(max_length=512, blank=True, verbose_name='text')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='updated at')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='author')
    is_active = models.BooleanField(default=False, verbose_name='is active', db_index=True)
