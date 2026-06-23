from django.conf import settings

from django.core.mail import EmailMultiAlternatives

from django.template.loader import render_to_string


def send_contact_notification(

    contact

):

    context = {

        "full_name": contact.full_name,

        "email": contact.email,

        "subject": contact.subject,

        "message": contact.message,

    }

    html_content = render_to_string(

        "contact/emails/admin_notification.html",

        context,

    )

    text_content = render_to_string(

        "contact/emails/admin_notification.txt",

        context,

    )

    email = EmailMultiAlternatives(

        subject=f"New Contact Message: {contact.subject}",

        body=text_content,

        from_email=settings.DEFAULT_FROM_EMAIL,

        to=[settings.CONTACT_RECEIVER_EMAIL],

    )

    email.attach_alternative(

        html_content,

        "text/html"

    )

    email.send()


def send_contact_confirmation(

    contact

):

    context = {

        "full_name": contact.full_name,

    }

    html_content = render_to_string(

        "contact/emails/visitor_confirmation.html",

        context,

    )

    text_content = render_to_string(

        "contact/emails/visitor_confirmation.txt",

        context,

    )

    email = EmailMultiAlternatives(

        subject="Thank You for Contacting Awoii Bob Willy",

        body=text_content,

        from_email=settings.DEFAULT_FROM_EMAIL,

        to=[contact.email],

    )

    email.attach_alternative(

        html_content,

        "text/html"

    )

    email.send()
