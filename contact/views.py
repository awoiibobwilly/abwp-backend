import logging

from rest_framework import generics

from .models import ContactMessage

from .serializers import ContactMessageSerializer

from .throttles import ContactRateThrottle

from .tasks import (
    send_admin_email_task,
    send_confirmation_email_task,
)


logger = logging.getLogger("contact")


class ContactMessageListCreateView(

    generics.ListCreateAPIView

):

    queryset = ContactMessage.objects.all()

    serializer_class = ContactMessageSerializer

    throttle_classes = [

        ContactRateThrottle

    ]

    throttle_scope = "contact"

    def perform_create(

        self,

        serializer

    ):

        contact = serializer.save()

        logger.info(

            f"New contact message from "

            f"{contact.full_name} "

            f"<{contact.email}>"

        )

        try:

            send_admin_email_task.delay(
                contact.id
            )

            send_confirmation_email_task.delay(
                contact.id
            )

            logger.info(

                f"Notification emails sent successfully "

                f"for {contact.email}"

            )

        except Exception as e:

            logger.exception(

                f"Email sending failed for "

                f"{contact.email}: {e}"

            )
