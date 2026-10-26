from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=100, verbose_name="Име")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата на създаване")

    def __str__(self):
        return self.name


class Story(models.Model):
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name='stories',
        verbose_name="Тема"
    )
    sources = models.ManyToManyField(
        'research.Source',
        blank=True,
        related_name='stories',
        verbose_name="Източници"
    )
    title = models.CharField(max_length=200, verbose_name="Заглавие")
    summary = models.TextField(blank=True, null=True, verbose_name="Резюме")
    status = models.CharField(
        max_length=20,
        choices=[
            ("draft", "Чернова"),
            ("in_progress", "В процес"),
            ("published", "Публикувана"),
        ],
        default="draft",
        verbose_name="Статус",
    )
    deadline = models.DateTimeField(blank=True, null=True, verbose_name="Краен срок")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата на създаване")

    def __str__(self):
        return self.title