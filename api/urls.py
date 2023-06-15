from django.urls import path
from . import views

app_name = "api"


urlpatterns = [
    # Excel
    path('excel/<int:month>/<int:year>/', views.ExcelAPIView.as_view()),

    # GET API DATA
    path('buttons/', views.ButtonAPIView.as_view(), name='buttons'),
    path('contents/', views.ContentAPIView.as_view(), name='contents'),

    # region
    path('regions/', views.RegionAPIView.as_view(), name='regions'),
    path('region_detail/<int:id>/', views.RegionDetailAPIView.as_view(), name='region_detail'),

    # path('region_by_name/', views.RegionByNameAPIView.as_view()),
    path('region_by_name/<str:name>/', views.RegionByNameAPIView.as_view(), name='region_by_name'),

    # shop
    path('shops/', views.ShopAPIView.as_view(), name='shops'),
    path('shop_detail/<int:id>/', views.ShopDetailAPIView.as_view(), name='shop_detail'),

    # path('shops_by_region_id/', views.ShopByRegionAPIView.as_view()),
    path('shops_by_region/<int:region>/', views.ShopByRegionAPIView.as_view(), name='shops_by_region'),

    path('shop_by_name/<str:name>/', views.ShopByNameAPIView.as_view(), name='shop_by_name'),

    # department
    path('departments/', views.DepartmentAPIView.as_view(), name='departments'),
    path('department_detail/<int:id>/', views.DepartmentDetailAPIView.as_view(), name='department_detail'),

    # path('department_by_title/', views.DepartmentByTitleAPIView.as_view()),
    path('department_by_title/<str:title>/', views.DepartmentByTitleAPIView.as_view(), name='department_by_title'),

    # problem
    path('problems/', views.ProblemAPIView.as_view(), name='problems'),
    path('problem_detail/<int:id>/', views.ProblemDetailAPIView.as_view(), name='problem_detail'),

    # path('problem_by_title/', views.ProblemByTitleAPIView.as_view()),
    path('problem_by_title/<str:title>/', views.ProblemByTitleAPIView.as_view(), name='problem_by_title'),

    # disparity
    path('disparities/', views.DisparityAPIView.as_view(), name='disparities'),
    path('disparity_detail/<int:id>/', views.DisparityDetailAPIView.as_view(), name='disparity_detail'),

    # path('disparities_by_problem_id/', views.DisparityByProblemAPIView.as_view()),
    path('disparities_by_problem/<int:problem>/', views.DisparityByProblemAPIView.as_view(), name='disparities_by_problem'),

    # path('disparity_by_title_problem_id/', views.DisparityByTitleAPIView.as_view()),
    path('disparity_by_title/', views.DisparityByTitleAPIView.as_view(), name='disparity_by_title'),

    # Client API
    path('clients/', views.ClientAPIView.as_view(), name='clients'),

    # Admin API
    path('admin_check_violation/<int:id>/', views.AdminCheckViolationAPIView.as_view(), name='admin_check_violation'),
    path('admin_check_excel/', views.AdminCheckExcelAPIView.as_view(), name='admin_check_excel'),

    # Violation API
    # path('', include(router.urls)),
    path('violations/', views.ViolationAPIView.as_view(), name='violations'),
    path('violations_days/<int:days>/', views.ViolationDaysAPIView.as_view(), name='violations_days'),
    path('violation_detail/<int:id>/', views.ViolationDetailAPIView.as_view(), name='violation_detail'),
    path('violation_response_detail/<int:id>/', views.ViolationResponseAPIView.as_view(), name='violation_response_detail'),
]
