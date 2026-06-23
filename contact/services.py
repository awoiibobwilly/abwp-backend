from django.conf import settings
from django.core.mail import send_mail


def send_contact_notification(contact):

    subject = (
        f"New Contact Message: "
        f"{contact.subject}"
    )

    message = f"""
You have received a new message.

Name:
{contact.full_name}

Email:
{contact.email}

Subject:
{contact.subject}

Message:
{contact.message}
"""

    send_mail(

        subject,

        message,

        settings.DEFAULT_FROM_EMAIL,

        [settings.CONTACT_RECEIVER_EMAIL],

        fail_silently=False,

    )


def send_contact_confirmation(contact):

    subject = (
        "Thank you for contacting "
        "Awoii Bob Willy"
    )

    message = f"""
Dear {contact.full_name},

Thank you for reaching out.

Your message has been received
successfully and I will respond
as soon as possible.

Regards,

Awoii Bob Willy
"""

    send_mail(

        subject,

        message,

        settings.DEFAULT_FROM_EMAIL,

        [contact.email],

        fail_silently=True,

    )

