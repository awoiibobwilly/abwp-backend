from rest_framework.permissions import AllowAny


class PublicPermission(AllowAny):
    """
    Default permission for all public
    portfolio endpoints.
    """

    pass