from rest_framework.exceptions import APIException


class EmployeeNotFoundError(APIException):
    default_detail = "Employee not found in the database."
    status_code = 400


class ExistingContractError(APIException):
    default_detail = "Employee already has a contract"
    status_code = 409