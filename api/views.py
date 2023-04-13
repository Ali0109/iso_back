from firebase_admin import messaging
from openpyxl import Workbook

from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from main import settings
from . import models, serializers, helpers, utils, exceptions


# Button
class ButtonAPIView(generics.ListAPIView):
    queryset = models.Button.objects.all()
    serializer_class = serializers.ButtonSerializer


# Content
class ContentAPIView(generics.ListAPIView):
    queryset = models.Content.objects.all()
    serializer_class = serializers.ContentSerializer


# Regions API -------------------------------------
class RegionAPIView(generics.ListAPIView):
    queryset = models.Region.objects.all()
    serializer_class = serializers.RegionSerializer


class RegionByNameAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.RegionSerializer
    lookup_url_kwarg = {"name": "name"}

    def get_queryset(self):
        try:
            queryset = models.Region.objects.get(name=self.kwargs['name'])
            return queryset
        except models.Region.DoesNotExist:
            raise exceptions.RegionDoesNotExist()

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=False)
        return Response(serializer.data)


class RegionDetailAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.RegionSerializer
    lookup_url_kwarg = {"id": "id"}

    def get_queryset(self):
        try:
            queryset = models.Region.objects.get(id=self.kwargs['id'])
            return queryset
        except models.Region.DoesNotExist:
            raise exceptions.RegionDoesNotExist()

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=False)
        return Response(serializer.data)


# Shops API -------------------------------------
class ShopAPIView(generics.ListAPIView):
    queryset = models.Shop.objects.all()
    serializer_class = serializers.ShopSerializer


class ShopDetailAPIView(generics.RetrieveAPIView):
    serializer = serializers.ShopSerializer
    lookup_url_kwarg = {"id": "id"}

    def get_queryset(self):
        try:
            queryset = models.Shop.objects.get(id=self.kwargs['id'])
            return queryset
        except models.Shop.DoesNotExist:
            raise exceptions.ShopDoesNotExist()

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer(queryset, many=False)
        return Response(serializer.data)


class ShopByRegionAPIView(generics.ListAPIView):
    serializer_class = serializers.ShopSerializer
    lookup_url_kwarg = {"region": "region"}

    def get_queryset(self):
        queryset = models.Shop.objects.filter(region_id=self.kwargs['region'])
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class ShopByNameAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.ShopSerializer
    lookup_url_kwarg = {"name": "name"}

    def get_queryset(self):
        try:
            queryset = models.Shop.objects.get(name=self.kwargs['name'])
            return queryset
        except models.Shop.DoesNotExist:
            raise exceptions.ShopDoesNotExist()

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=False)
        return Response(serializer.data)


# Departments API -------------------------------------
class DepartmentAPIView(generics.ListAPIView):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer


class DepartmentDetailAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.DepartmentSerializer
    lookup_url_kwarg = {"id": "id"}

    def get_queryset(self):
        try:
            queryset = models.Department.objects.get(id=self.kwargs['id'])
            return queryset
        except models.Department.DoesNotExist:
            raise exceptions.DepartmentDoesNotExist()

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=False)
        return Response(serializer.data)


class DepartmentByTitleAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.DepartmentSerializer
    lookup_url_kwarg = {"title": "title"}

    def get_queryset(self):
        try:
            queryset = models.Department.objects.get(title=self.kwargs['title'])
            return queryset
        except models.Department.DoesNotExist:
            raise exceptions.DepartmentDoesNotExist()

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=False)
        return Response(serializer.data)


# Problems API -------------------------------------
class ProblemAPIView(generics.ListAPIView):
    queryset = models.Problem.objects.all()
    serializer_class = serializers.ProblemSerializer


class ProblemDetailAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.ProblemSerializer
    lookup_url_kwarg = {"id": "id"}

    def get_queryset(self):
        try:
            queryset = models.Problem.objects.get(id=self.kwargs['id'])
            return queryset
        except models.Problem.DoesNotExist:
            raise exceptions.ProblemDoesNotExist()

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=False)
        return Response(serializer.data)


class ProblemByTitleAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.ProblemSerializer
    lookup_url_kwarg = {"title": "title"}

    def get_queryset(self):
        try:
            queryset = models.Problem.objects.get(title=self.kwargs['title'])
            return queryset
        except models.Problem.DoesNotExist:
            raise exceptions.ProblemDoesNotExist()

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=False)
        return Response(serializer.data)


# Disparities API -------------------------------------
class DisparityAPIView(generics.ListAPIView):
    queryset = models.Disparity.objects.all()
    serializer_class = serializers.DisparitySerializer


class DisparityDetailAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.DisparitySerializer
    lookup_url_kwarg = {"id": "id"}

    def get_queryset(self):
        try:
            queryset = models.Disparity.objects.get(id=self.kwargs['id'])
            return queryset
        except models.Disparity.DoesNotExist:
            raise exceptions.DisparityDoesNotExist()

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=False)
        return Response(serializer.data)


class DisparityByProblemAPIView(generics.ListAPIView):
    serializer_class = serializers.DisparitySerializer
    lookup_url_kwarg = {"problem": "problem"}

    def get_queryset(self):
        queryset = models.Disparity.objects.filter(problem_id=self.kwargs['problem'])
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class DisparityByTitleAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.DisparitySerializer
    lookup_url_kwarg = {"title": "title"}

    def get_queryset(self):
        try:
            queryset = models.Disparity.objects.get(title=self.kwargs['title'])
            return queryset
        except models.Disparity.DoesNotExist:
            raise exceptions.DisparityDoesNotExist()

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=False)
        return Response(serializer.data)


# Client API -------------------------------------
class ClientAPIView(generics.ListCreateAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = serializers.ClientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ClientDetailAPIView(generics.RetrieveAPIView):
    serializer = serializers.ClientSerializer
    lookup_url_kwarg = {'id': 'id'}

    def get_queryset(self):
        try:
            queryset = models.Client.objects.get(id=self.kwargs['id'])
            return queryset
        except models.Client.DoesNotExist:
            raise exceptions.ClientDoesNotExist()

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer(queryset, many=False)
        return Response(serializer.data)


class AdminAPIView(generics.ListCreateAPIView):
    serializer = serializers.AdminSerializer

    def get_queryset(self):
        queryset = models.Admin.objects.filter(is_staff=1)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = serializers.AdminSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = serializers.AdminSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class AdminCheckViolationAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.AdminCheckViolationSerializer
    lookup_url_kwarg = {'id': 'id'}

    def get_queryset(self):
        try:
            models.Violation.objects.get(
                id=self.kwargs['id'],
                response_admin__tg_id=self.request.data['tg_id'],
                status_id=2,
            )
            raise exceptions.AuthorizedException()
        except models.Violation.DoesNotExist:
            raise exceptions.UnauthorizedException()


class AdminCheckExcelAPIView(generics.CreateAPIView):
    serializer_class = serializers.AdminCheckExcelSerializer

    def get_queryset(self):
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            queryset = models.Admin.objects.filter(
                tg_id=self.request.data['tg_id'],
            )
            return queryset
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset:
            raise exceptions.AuthorizedException()
        else:
            raise exceptions.UnauthorizedException()


# Status
class StatusAPIView(generics.ListAPIView):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


# Process
class ProcessAPIView(generics.ListAPIView):
    queryset = models.Process.objects.all()
    serializer_class = serializers.ProcessSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


# Violation API -------------------------------------
class ViolationAPIView(generics.ListCreateAPIView):
    queryset = models.Violation.objects.all()
    serializer = serializers.ViolationSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ViolationDetailAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.ViolationSerializer

    def get_queryset(self):
        try:
            queryset = models.Violation.objects.get(id=self.kwargs['id'])
            return queryset
        except models.Violation.DoesNotExist:
            raise exceptions.ViolationDoesNotExist()

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=False)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ViolationResponseAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.ViolationResponseSerializer
    lookup_url_kwarg = {'id': 'id'}

    def get_queryset(self):
        try:
            queryset = models.Violation.objects.get(id=self.kwargs['id'])
            return queryset
        except models.Violation.DoesNotExist:
            raise exceptions.ViolationDoesNotExist()

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=False)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ViolationDaysAPIView(generics.ListAPIView):
    serializer_class = serializers.ViolationSerializer
    lookup_url_kwarg = {'days': 'days'}

    def get_queryset(self):
        datetime_previous = helpers.time_helper.get_datetime_previous_by_days(days=self.kwargs['days'])

        queryset = models.Violation.objects.filter(created_at__gte=datetime_previous).all()
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


# Login
class LoginAPIView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.LoginSerializer
    lookup_url_kwarg = {"phone": "phone"}

    def get_queryset(self):
        try:
            queryset = models.Admin.objects.get_with_token_by_phone(phone=self.kwargs['phone'])
            return queryset
        except models.Admin.DoesNotExist:
            raise exceptions.AdminDoesNotExist()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=False)
        return Response(serializer.data)


class DeviceAPIView(generics.ListCreateAPIView):
    queryset = models.Device.objects.all()
    serializer_class = serializers.DeviceSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SendNotificationAPIView(generics.CreateAPIView):

    def create(self, request, *args, **kwargs):
        devices_all = list(models.Device.objects.filter(is_active=1).values_list('registration_id', flat=True))

        message = messaging.MulticastMessage(
            notification=messaging.Notification(
                title="test title",
                body="test body",
                image="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png",
            ),
            tokens=devices_all,
        )
        response = messaging.send_multicast(message)
        # is active=0 if deactivate device
        helpers.device_helper.response_deactivate_device(response, devices_all)

        return Response(response.success_count, status=status.HTTP_200_OK)


class ExcelAPIView(APIView):

    def get(self, request, month, year):
        wb = Workbook()

        created_at_from = helpers.excel_helper.generate_next_month(year, month)['from']
        created_at_to = helpers.excel_helper.generate_next_month(year, month)['to']

        days_in_month_list = helpers.excel_helper.days_in_month_func(year, month)

        excel = utils.ExcelUtils(
            year=year, month=month, wb=wb,
            created_at_from=created_at_from, created_at_to=created_at_to,
            days_in_month_list=days_in_month_list,
        )

        excel.report_market_func()
        excel.report_process_func()
        excel.report_department_func()
        excel.report_attendance_func()
        excel.report_general_func()
        # report_weeks_func()
        wb.active = wb['Отчет по маркетам']

        if int(month) < 10:
            month = f"0{month}"

        excel_name = f"media/excel/report_data_{month}_{year}.xlsx"
        wb.save(excel_name)

        serializer_dict = {
            "file": f"{settings.CSRF_TRUSTED_ORIGINS[0]}/{excel_name}",
        }
        serializer = serializers.ExcelSerializer(serializer_dict, many=False)

        message = serializer.data
        status_code = status.HTTP_200_OK
        return Response(message, status=status_code)
