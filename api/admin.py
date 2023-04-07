from django.contrib import admin
from . import models


@admin.register(models.Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]


@admin.register(models.Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'region',
    ]
    list_filter = ["region"]


@admin.register(models.Button)
class ButtonAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "key",
        "title",
    ]


@admin.register(models.Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "key",
        "title",
    ]


@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
    ]


@admin.register(models.Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
    ]


@admin.register(models.Disparity)
class DisparityAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "problem",
    ]
    list_filter = ["problem"]


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "phone",
        "tg_id",
        "status",
        "created_at",
        "updated_at",
    ]


@admin.register(models.Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "phone",
        "name",
        "tg_id",
        "is_staff",
        "is_superuser",
        "is_active",
        "created_at",
        "updated_at",
    ]


@admin.register(models.Violation)
class ViolationAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "client",
        "region",
        "shop",
        "department",
        "problem",
        "disparity",
        "comment",
        "photo",
        "is_no_violation",
        "is_active",
        "created_at",
        "updated_at",
    ]
    list_filter = [
        "region",
        "shop",
        "department",
        "problem",
        "disparity",
        "is_active",
    ]


@admin.register(models.Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
    ]


