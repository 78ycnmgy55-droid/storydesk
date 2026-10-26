from django.db import models
from stories.models import Story

class Source(models.Model):
    name = models.CharField(max_length=150, verbose_name="Име")
    source_type = models.CharField(
        max_length=20,
        choices=[
            ("expert", "Експерт"),
            ("institution", "Институция"),
            ("document", "Документ"),
            ("website", "Уебсайт"),
        ],
        verbose_name="Вид на източника",
    )
    organization = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="Организация",
    )
    contact_info = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Данни за контакт",
    )
    notes = models.TextField(
        blank=True,
        verbose_name="Бележки",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата на създаване",
    )

    def __str__(self):
        return self.name


class Note(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=150, verbose_name="Заглавие")
    content = models.TextField(verbose_name="Съдържание")
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата на създаване",
    )

    def __str__(self):
        return self.title