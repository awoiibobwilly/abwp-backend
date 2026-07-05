from rest_framework import generics

from about.models import CoreValues
from about.serializers import CoreValuesSerializer


class CoreValuesDetailAPIView(generics.RetrieveAPIView):
    serializer_class = CoreValuesSerializer

    def get_object(self):
        return CoreValues.objects.filter(
            is_active=True
        ).order_by("-updated_at").first()