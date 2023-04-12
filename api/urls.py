from django.urls import path
from . import views

app_name = "api"


urlpatterns = [
    # Excel
    path('excel/<int:month>/<int:year>/', views.ExcelAPIView.as_view()),

    # GET API DATA
    path('buttons/', views.ButtonAPIView.as_view()),
    path('contents/', views.ContentAPIView.as_view()),

    # region
    path('regions/', views.RegionAPIView.as_view()),
    path('region_detail/<int:id>/', views.RegionDetailAPIView.as_view()),

    # path('region_by_name/', views.RegionByNameAPIView.as_view()),
    path('region_by_name/<str:name>/', views.RegionByNameAPIView.as_view()),

    # shop
    path('shops/', views.ShopAPIView.as_view()),
    path('shop_detail/<int:id>/', views.ShopDetailAPIView.as_view()),

    # path('shops_by_region_id/', views.ShopByRegionAPIView.as_view()),
    path('shops_by_region/<int:region>/', views.ShopByRegionAPIView.as_view()),

    path('shop_by_name/<str:name>/', views.ShopByNameAPIView.as_view()),

    # department
    path('departments/', views.DepartmentAPIView.as_view()),
    path('department_detail/<int:id>/', views.DepartmentDetailAPIView.as_view()),

    # path('department_by_title/', views.DepartmentByTitleAPIView.as_view()),
    path('department_by_title/<str:title>/', views.DepartmentByTitleAPIView.as_view()),

    # problem
    path('problems/', views.ProblemAPIView.as_view()),
    path('problem_detail/<int:id>/', views.ProblemDetailAPIView.as_view()),

    # path('problem_by_title/', views.ProblemByTitleAPIView.as_view()),
    path('problem_by_title/<str:title>/', views.ProblemByTitleAPIView.as_view()),

    # disparity
    path('disparities/', views.DisparityAPIView.as_view()),
    path('disparity_detail/<int:id>/', views.DisparityDetailAPIView.as_view()),

    # path('disparities_by_problem_id/', views.DisparityByProblemAPIView.as_view()),
    path('disparities_by_problem/<int:problem>/', views.DisparityByProblemAPIView.as_view()),

    # path('disparity_by_title_problem_id/', views.DisparityByTitleAPIView.as_view()),
    path('disparity_by_title/', views.DisparityByTitleAPIView.as_view()),

    # Client API
    path('clients/', views.ClientAPIView.as_view()),

    # Admin API
    path('admin_check_violation/<int:id>/', views.AdminCheckViolationAPIView.as_view()),
    path('admin_check_excel/', views.AdminCheckExcelAPIView.as_view()),

    # Violation API
    # path('', include(router.urls)),
    path('violations/', views.ViolationAPIView.as_view()),
    path('violations_days/<int:days>/', views.ViolationDaysAPIView.as_view()),
    path('violation_detail/<int:id>/', views.ViolationDetailAPIView.as_view()),
    path('violation_response_detail/<int:id>/', views.ViolationResponseAPIView.as_view()),
]
