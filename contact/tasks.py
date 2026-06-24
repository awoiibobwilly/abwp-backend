from celery import shared_task

from .models import ContactMessage

from .services import (
    send_contact_notification,
    send_contact_confirmation,
)


@shared_task
def send_admin_email_task(
    contact_id
):

    contact = ContactMessage.objects.get(
        id=contact_id
    )

    send_contact_notification(
        contact
    )


@shared_task
def send_confirmation_email_task(
    contact_id
):

    contact = ContactMessage.objects.get(
        id=contact_id
    )

    send_contact_confirmation(
        contact
    )
