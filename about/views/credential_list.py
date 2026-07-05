from rest_framework import generics

from about.models import Credential
from about.serializers import CredentialSerializer


class CredentialListAPIView(generics.ListAPIView):
    serializer_class = CredentialSerializer

    def get_queryset(self):
        return Credential.objects.filter(
            is_active=True
        ).order_by("group", "display_order", "id")