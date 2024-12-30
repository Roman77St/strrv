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

class CRContent(models.Model):
    nosological_form = models.OneToOneField(to=Recomendation, on_delete=models.PROTECT, related_name='cr_content',
                                            verbose_name='нозологическая форма')
    list_of_abbreviations = models.TextField(blank=True, verbose_name="Список сокращений")
    terms_and_definitions = models.TextField(blank=True, verbose_name="Термины и определения")
    brief_information = models.TextField(blank=True, verbose_name="Краткая информация")
    definition_of_state = models.TextField(blank=True, verbose_name="Определение заболевания")
    etiology_and_pathogenesis = models.TextField(blank=True, verbose_name="Этиология и патогенез")
    epidemiology = models.TextField(blank=True, verbose_name="Эпидемиология")
    coding = models.TextField(blank=True, verbose_name="Особенности кодирования")
    classification = models.TextField(blank=True, verbose_name="Классификация")
    clinical_picture = models.TextField(blank=True, verbose_name="Клиническая картина")
    diagnostics = models.TextField(blank=True, verbose_name="Диагностика")
    complaints_and_anamnesis = models.TextField(blank=True, verbose_name="Жалобы и анамнез")
    physical_examination = models.TextField(blank=True, verbose_name="Физикальное обследование")
    laboratory_research = models.TextField(blank=True, verbose_name="Лабораторные исследования")
    instrumental_research = models.TextField(blank=True, verbose_name="Инструментальные исследования")
    other_studies = models.TextField(blank=True, verbose_name="Иные исследования")
    treatment = models.TextField(blank=True, verbose_name="Лечение")
    rehabilitation = models.TextField(blank=True, verbose_name="Реабилитация")
    prevention = models.TextField(blank=True, verbose_name="Профилактика")
    organization_of_medical_care = models.TextField(blank=True, verbose_name="Организация оказания мед. помощи")
    additional_information = models.TextField(blank=True, verbose_name="Доп. информация")
    quality_assessment = models.TextField(blank=True, verbose_name="Оценка качества")

    class Meta: 
        db_table = 'cr_content'
        verbose_name = "Клинические рекомендации - контент"
        ordering = ("id",)

    def __str__(self):
        return str(self.nosological_form)
    
class CRTableOfContent(models.Model):
    title = models.CharField(max_length=200, verbose_name="Раздел кратко")
    text = models.CharField(max_length=200, verbose_name="Раздел полное написание", blank=True)
    link = models.CharField(max_length=100, blank=True, verbose_name='ID для внутренней ссылки')
    class Meta: 
        db_table = 'cr_table_of_content'
        verbose_name = "Клинические рекомендации - оглавление"

    def __str__(self):
        return str(self.title)