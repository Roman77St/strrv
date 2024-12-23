from django.db import models
from django.urls import reverse

from multiselectfield import MultiSelectField



class Recomendation(models.Model):

    name = models.CharField(max_length=200, unique=True, verbose_name="Нозололическая форма")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, verbose_name="Слаг"
    )
    rec_id = models.CharField(max_length=10, unique=True, verbose_name="ID")
    age_category = MultiSelectField(
        max_length=100,
        blank=True,
        verbose_name="Возрастная категория",
        choices=[('Adult', "Взрослые"), ('Child', "Дети")],
    )
    speciality = models.CharField(
        max_length=100, blank=True, verbose_name="Специальность"
    )
    year_of_approval = models.PositiveIntegerField(
        verbose_name="Год утверждения", blank=True
    )
    year_of_revision = models.PositiveIntegerField(
        verbose_name="Год пересмотра", blank=True
    )
    developer = models.TextField(blank=True, verbose_name="Разработчик")
    status = models.CharField(
        max_length=50,
        choices=[("Одобрены", "Одобрены"), ("В разработке", "В разработке"), ("Отменены", "Отменены")],
        verbose_name="Статус",
    )

    class Meta:
        db_table = "recomendation"
        verbose_name = "Клиническая рекомендация"
        verbose_name_plural = "Клинические рекомендации"
        ordering = ("name",)

    def get_absolute_url(self):
        return reverse("ophthalmology:recomend_item", kwargs={"recomend_slug": self.slug})

    def __str__(self):
        return str(self.name)
