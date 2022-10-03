from rest_framework.exceptions import APIException


class ProfileNotFound(APIException):
    status_code = 404
    default_detail = "The requested Profile does not exist"


class NotYourProfile(APIException):
    status_code = 403
    default_detail = "You cannot edit profile that does not belong to you"
