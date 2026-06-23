from rest_framework import generics

from .models import ContactMessage
from .serializers import ContactMessageSerializer

from .services import (
    send_contact_notification,
    send_contact_confirmation,
)

import logging

logger = logging.getLogger(__name__)


class ContactMessageListCreateView(

    generics.ListCreateAPIView

):

    queryset = ContactMessage.objects.all()

    serializer_class = ContactMessageSerializer


    def perform_create(self, serializer):

        contact = serializer.save()

        try:

            send_contact_notification(contact)

            send_contact_confirmation(contact)

        except Exception as e:

            logger.exception(

                f"Email sending failed: {e}"

            )
