from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django_softdelete.models import SoftDeleteModel, SoftDeleteQuerySet
from django.contrib.auth.models import PermissionsMixin
from rest_framework.authtoken.models import Token

from main.settings import base


class Status(SoftDeleteModel):
    title = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Process(SoftDeleteModel):
    title = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = 'Процесс'
        verbose_name_plural = 'Процессы'


class CustomAdminManager(BaseUserManager):
    def get_queryset(self):
        return SoftDeleteQuerySet(self.model).filter(is_deleted=False)

    def create_token(self, user_id):
        if user_id == 1:
            token, is_created = Token.objects.get_or_create(
                user_id=user_id,
                key=base.DEFAULT_AUTH_TOKEN,
            )
        else:
            token, is_created = Token.objects.get_or_create(user_id=user_id)
        return token

    def create_superuser(self, phone, password, **other_fields):
        user = self.create_is_staff(phone=phone, password=password, **other_fields)
        user.is_superuser = True
        return user

    def create_is_staff(self, phone, password, **other_fields):
        user = self.create_user(phone=phone, password=password, **other_fields)
        user.is_staff = True
        self.create_token(user_id=user.id)
        return user

    def create_user(self, phone, password, **other_fields):
        if not phone:
            raise ValueError("You must provide a phone number")
        if not password:
            raise ValueError("You must provide a password")

        user = self.model(phone=phone, **other_fields)
        user.set_password(password)
        user.is_active = True
        user.save()
        return user

    def get_with_token_by_phone(self, phone):
        admin = self.get_queryset().get(phone=phone)
        token = self.create_token(user_id=admin.id)
        admin.token = token.key
        return admin


class Admin(SoftDeleteModel, AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    tg_id = models.CharField(max_length=40)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomAdminManager()

    def __str__(self):
        return str(self.phone)

    class Meta:
        ordering = ['id']
        verbose_name = 'администратора'
        verbose_name_plural = 'Администраторы'


class Button(SoftDeleteModel):
    key = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.key

    class Meta:
        ordering = ['id']
        verbose_name = 'Кнопку'
        verbose_name_plural = 'Кнопки'


class Content(SoftDeleteModel):
    key = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.key

    class Meta:
        ordering = ['id']
        verbose_name = 'Контент'
        verbose_name_plural = 'Контенты'


class Region(SoftDeleteModel):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'


class Shop(SoftDeleteModel):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.region}"

    class Meta:
        ordering = ['id']
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'


class Department(SoftDeleteModel):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'


class Problem(SoftDeleteModel):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = 'Проблему'
        verbose_name_plural = 'Проблемы'


class Disparity(SoftDeleteModel):
    title = models.CharField(max_length=100)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.problem}"

    class Meta:
        ordering = ['id']
        verbose_name = 'Несоответствие'
        verbose_name_plural = 'Несоответствия'


class Client(SoftDeleteModel):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=255, unique=True)
    tg_id = models.CharField(max_length=40)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name = 'Клиента'
        verbose_name_plural = 'Клиенты'


class Violation(SoftDeleteModel):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    problem = models.ForeignKey(Problem, on_delete=models.SET_NULL, null=True, blank=True)
    disparity = models.ForeignKey(Disparity, on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='uploads/photo/', null=True, blank=True)
    response_admin = models.ForeignKey("Admin", on_delete=models.SET_NULL, null=True, blank=True)
    response_person_description = models.TextField(null=True, blank=True)
    response_result_photo = models.ImageField(upload_to='uploads/photo/response/', null=True, blank=True)
    status = models.ForeignKey("Status", on_delete=models.SET_NULL, null=True, default=1)
    process = models.ForeignKey("Process", on_delete=models.SET_NULL, null=True, blank=True)
    is_no_violation = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.is_active = True
        super(Violation, self).save()

    def __str__(self):
        return f"{self.client} - {self.region}"

    class Meta:
        ordering = ['-id']
        verbose_name = 'Нарушение'
        verbose_name_plural = 'Нарушения'


class Device(SoftDeleteModel):
    device_id = models.CharField(max_length=255)
    registration_id = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    user = models.ForeignKey(Admin, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.device_id} - {self.user}"

    class Meta:
        ordering = ['-id']
        verbose_name = 'Устройство'
        verbose_name_plural = 'Устройства'
