from django.db import models
from stories.models import Story


class Task(models.Model):
    story = models.ForeignKey(
        Story,
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name='Материал',
    )
    title = models.CharField(max_length=200, verbose_name='Заглавие')
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание',
    )
    due_date = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Краен срок',
    )
    is_completed = models.BooleanField(
        default=False,
        verbose_name='Изпълнена',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата на създаване',
    )

    def __str__(self):
        return self.title