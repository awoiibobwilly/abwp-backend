import logging

from rest_framework import generics

from .models import ContactMessage

from .serializers import ContactMessageSerializer

from .throttles import ContactRateThrottle

from .services import (
    send_contact_notification,
    send_contact_confirmation,
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


        # Log successful database save
        logger.info(

            f"New contact message from "

            f"{contact.full_name} "

            f"<{contact.email}>"

        )


        try:

            send_contact_notification(contact)

            send_contact_confirmation(contact)


            # Log successful email delivery
            logger.info(

                f"Notification emails sent successfully "

                f"for {contact.email}"

            )


        except Exception as e:

            # Log email failures
            logger.exception(

                f"Email sending failed for "

                f"{contact.email}: {e}"

            )
