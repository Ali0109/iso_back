from rest_framework.exceptions import APIException


class AdminDoesNotExist(APIException):
    status_code = 404
    default_detail = 'Admin does not exist'
    default_code = 'admin_does_not_exist'


class ClientDoesNotExist(APIException):
    status_code = 404
    default_detail = 'Client does not exist'
    default_code = 'client_does_not_exist'


class RegionDoesNotExist(APIException):
    status_code = 404
    default_detail = 'Region does not exist'
    default_code = 'region_does_not_exist'


class ShopDoesNotExist(APIException):
    status_code = 404
    default_detail = 'Shop does not exist'
    default_code = 'shop_does_not_exist'


class DepartmentDoesNotExist(APIException):
    status_code = 404
    default_detail = 'Department does not exist'
    default_code = 'department_does_not_exist'


class ProblemDoesNotExist(APIException):
    status_code = 404
    default_detail = 'Problem does not exist'
    default_code = 'problem_does_not_exist'


class DisparityDoesNotExist(APIException):
    status_code = 404
    default_detail = 'Disparity does not exist'
    default_code = 'disparity_does_not_exist'


class ViolationDoesNotExist(APIException):
    status_code = 404
    default_detail = 'Violation does not exist'
    default_code = 'violation_does_not_exist'


class AuthorizedException(APIException):
    status_code = 200
    default_detail = 'Authorized'
    default_code = 'authorized'


class UnauthorizedException(APIException):
    status_code = 401
    default_detail = 'Unauthorized'
    default_code = 'unauthorization'
