import logging

from celery import shared_task

from .models import ContactMessage

from .services import (
    send_contact_notification,
    send_contact_confirmation,
)


logger = logging.getLogger("contact")


@shared_task(

    bind=True,

    max_retries=3,

    autoretry_for=(Exception,),
    retry_backoff=True,
    retry_backoff_max=600,
    retry_jitter=True

)
def send_admin_email_task(

    self,

    contact_id

):

    try:

        contact = ContactMessage.objects.get(

            id=contact_id

        )

        logger.info(

            f"Starting admin notification task "

            f"for {contact.email}"

        )

        send_contact_notification(

            contact

        )

        logger.info(

            f"Admin notification sent "

            f"successfully for {contact.email}"

        )

    except ContactMessage.DoesNotExist:

        logger.error(

            f"Contact message {contact_id} "

            f"does not exist."

        )

    except Exception as e:

        logger.exception(

            f"Admin email task failed "

            f"for contact {contact_id}: {e}"

        )

        raise self.retry(

            exc=e

        )


@shared_task(

    bind=True,

    max_retries=3,

    autoretry_for=(Exception,),
    retry_backoff=True,
    retry_backoff_max=600,
    retry_jitter=True

)
def send_confirmation_email_task(

    self,

    contact_id

):

    try:

        contact = ContactMessage.objects.get(

            id=contact_id

        )

        logger.info(

            f"Starting confirmation email task "

            f"for {contact.email}"

        )

        send_contact_confirmation(

            contact

        )

        logger.info(

            f"Confirmation email sent "

            f"successfully to {contact.email}"

        )

    except ContactMessage.DoesNotExist:

        logger.error(

            f"Contact message {contact_id} "

            f"does not exist."

        )

    except Exception as e:

        logger.exception(

            f"Confirmation email task failed "

            f"for contact {contact_id}: {e}"

        )

        raise self.retry(

            exc=e

        )
