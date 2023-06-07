from django.db import models
from django.utils import timezone

from traffic.app.utils import get_file_path


class UserGroup(models.Model):
    """Справочник - Роль пользователя"""

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Справочник - Роль пользователяв"
        verbose_name_plural = "Справочник - Роль пользователя"

    def __str__(self):
        return "{}".format(self.name)


class UserGroupConst:
    ADMIN = "ADMIN"
    CLIENT = "CLIENT"


class User(models.Model):
    """Пользователь"""

    name = models.CharField("ФИО", max_length=100, blank=True)
    group = models.ForeignKey(
        "UserGroup",
        on_delete=models.PROTECT,
        related_name="user",
    )
    email = models.EmailField(unique=True)
    password = models.CharField("Пароль", max_length=100, blank=True)
    created_date = models.DateTimeField("Дата регистрации", default=timezone.now)
    last_login = models.DateTimeField("Дата последней авторизации", blank=True, null=True)
    contract_number = models.CharField('Номер договора', max_length=100, blank=True)
    mobile_phone = models.CharField("Телефон", max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return "{}".format(self.email)


class UserFiles(models.Model):
    """Пользовательский файл"""

    file = models.FileField(
        verbose_name="Файл",
        upload_to=get_file_path,
        null=True,
        blank=True,
    )
    name = models.CharField("Название файла", max_length=300, blank=True, null=True)
    user = models.ForeignKey(
        "User",
        on_delete=models.PROTECT,
        related_name="user_files",
    )
    type = models.ForeignKey(
        "FileType",
        on_delete=models.PROTECT,
        related_name="user_file_type",
        blank=True,
        null=True,
    )
    created_date = models.DateTimeField("Дата загрузки файла", default=timezone.now)

    class Meta:
        verbose_name = "Пользовательский файл"
        verbose_name_plural = "Пользовательские файлы"

    def __str__(self):
        return "{}".format(self.pk)


class FileType(models.Model):
    """Справочник - Типы файлов"""

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Справочник - Типы файлов"
        verbose_name_plural = "Справочник - Типы файлов"

    def __str__(self):
        return "{}".format(self.name)


class FileTypeConst:
    UPLOAD_XLSX = "upload_xlsx"
    DOWNLOAD_PDF = "download_pdf"
    UPLOAD_VIDEO = "upload_video"
    DAY_TRAFFIC_GRAPH = "day_traffic_graph"
    AVERAGE_TRAFFIC_GRAPH = "average_traffic_graph"


class Location(models.Model):
    """Локация, на которой подсчитывается трафик"""

    address = models.TextField(
        verbose_name='Адрес локации для подсчета трафика',
        blank=True,
        null=True,
    )
    user = models.ForeignKey(
        User,
        verbose_name='Клиент',
        on_delete=models.PROTECT,
        related_name="location",
        blank=True,
        null=True,
    )
    created_date = models.DateTimeField("Дата загрузки файла", default=timezone.now)
    admin = models.ForeignKey(
        User,
        verbose_name='Администратор',
        on_delete=models.PROTECT,
        related_name="location_admin",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return "{}".format(self.address)


class Camera(models.Model):
    """Камера"""

    focus = models.DecimalField(
        verbose_name='Фокусное расстояние',
        max_digits=3,
        decimal_places=3,
        null=True,
        blank=True
    )
    fps = models.DecimalField(
        verbose_name='Кол-во адров в секунду',
        max_digits=15,
        decimal_places=3,
        null=True,
        blank=True
    )
    name = models.CharField(max_length=50)
    location = models.ForeignKey(
        Location,
        verbose_name='Локация, на которой установлена камера',
        on_delete=models.PROTECT,
        related_name="location_camera",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Камера"
        verbose_name_plural = "Камеры"

    def __str__(self):
        return "{}".format(self.name)


class Report(models.Model):
    """Отчёт по анализу трафика"""

    start_date = models.DateTimeField(
        "Начало периода подсчёта",
        default=timezone.now
    )
    end_date = models.DateTimeField(
        "Конец периода подсчёта",
        null=True,
        blank=True
    )
    location = models.ForeignKey(
        Location,
        verbose_name='Локация, на которой ведэтся подсчет',
        on_delete=models.PROTECT,
        related_name="location_report",
        blank=True,
        null=True,
    )
    model_report = models.TextField(
        verbose_name='JSON данные',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Отчёт по анализу трафика"
        verbose_name_plural = "Отчёты по анализу трафика"

    def __str__(self):
        return "{}".format(self.location)
