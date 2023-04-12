from rest_framework import serializers

from . import models, helpers


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Admin
        fields = [
            "id",
            "phone",
            "name",
            "password",
            "is_staff",
            "is_superuser",
            "is_active",
            "created_at",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        try:
            admin = models.Admin.objects.get(phone=validated_data['phone'])
        except models.Admin.DoesNotExist:
            admin = models.Admin.objects.create_is_staff(**validated_data)
        return admin


class AdminCheckViolationSerializer(serializers.ModelSerializer):
    tg_id = serializers.IntegerField(source='response_admin.tg_id')

    class Meta:
        model = models.Violation
        fields = ['id', 'tg_id']


class AdminCheckExcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Admin
        fields = ['tg_id']


# Button
class ButtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Button
        fields = ("id", "key", "title")


# Content
class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Content
        fields = ("id", "key", "title")


# Region
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Region
        fields = ("id", "name")


# Shop
class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shop
        fields = [
            "id",
            "name",
            "region",
        ]


# Department
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = ("id", "title")


# Problem
class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Problem
        fields = ("id", "title")


# Disparity
class DisparitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Disparity
        fields = ("id", "title", "problem")
        extra_kwargs = {
            'title': {'read_only': True}
        }


# Client
class ClientSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=255)
    class Meta:
        model = models.Client
        fields = (
            "id",
            "name",
            "phone",
            "tg_id",
        )

    def create(self, validated_data):
        try:
            client = models.Client.global_objects.get(phone=validated_data['phone'])
            if client.is_deleted == 1:
                client.is_deleted = 0
                client.save()
        except models.Client.DoesNotExist:
            client = models.Client.objects.create(**validated_data)
        return client


# Status
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Status
        fields = [
            "id",
            "title",
        ]


# Process
class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Process
        fields = (
            "id",
            "title",
        )


# Violation
class ViolationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Violation
        fields = (
            # Violation create
            "id",
            "client",
            "region",
            "shop",
            "department",
            "problem",
            "disparity",
            "comment",
            "photo",

            # Violation response admin
            "response_admin",
            "response_person_description",
            "response_result_photo",
            "status",
            "process",

            "is_no_violation",
            "is_active",
            "created_at",
        )

    def create(self, validated_data):
        violation = models.Violation.objects.create(**validated_data)
        return violation

    def update(self, instance, validated_data):
        instance = helpers.violation_helper.update(instance=instance, validated_data=validated_data)
        return instance


class ViolationResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Violation
        fields = [
            'status',
            'response_admin',
            'response_person_description',
            'response_result_photo',
        ]

    def update(self, instance, validated_data):
        instance = helpers.violation_helper.update(instance=instance, validated_data=validated_data)
        return instance


class ExcelSerializer(serializers.Serializer):
    file = serializers.CharField(max_length=255)


class LoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=200)

    class Meta:
        model = models.Admin
        fields = [
            'id',
            'name',
            'phone',
            'token',
            'is_staff',
            'is_superuser',
            'is_active',
            'created_at',
        ]


# Device
class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Device
        fields = (
            "id",
            "is_active",
            "device_id",
            "registration_id",
            "type",
            "user",
            "created_at",
        )
        extra_kwargs = {
            "device_id": {"required": True},
            "user": {"required": True},
            "is_active": {"default": True},
        }

    def create(self, validated_data):
        device = models.Device.objects.create(**validated_data)
        return device
