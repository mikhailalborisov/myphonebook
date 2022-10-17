from django.db import models
from django.urls import reverse


# Create your models here.
class PhoneBook(models.Model):
    first_name = models.CharField(
        max_length=100,
        help_text="Введите имя",
        verbose_name="Имя",
    )
    last_name = models.CharField(
        max_length=100,
        help_text="Введите фамилию",
        verbose_name="Фамилия",
    )
    note = models.CharField(
        max_length=400,
        help_text="Введите заметку",
        verbose_name="Заметка",
    )
    phone = models.CharField(
        max_length=15,
        help_text="Введите номер телефона",
        verbose_name="Номер телефона",
    )
    favourites = models.BooleanField(
        help_text="Добавить в избранное", verbose_name="Избранное"
    )
    date_of_creation = models.DateField(
        help_text="Введите дату создания контакта",
        verbose_name="Дaтa создания контакта",
        null=True,
        blank=True,
    )

    def get_absolute_url(self):
        return reverse("phonebook-detail", kwargs={"pk": self.pk})
