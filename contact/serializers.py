from datetime import timedelta

from django.utils import timezone

from rest_framework import serializers

from .models import ContactMessage


class ContactMessageSerializer(

    serializers.ModelSerializer

):

    class Meta:

        model = ContactMessage

        fields = "__all__"

        read_only_fields = (

            "id",

            "is_read",

            "created_at",

        )

        extra_kwargs = {

            "full_name": {

                "error_messages": {

                    "required": "Please enter your full name.",

                    "blank": "Full name cannot be blank.",

                }

            },

            "email": {

                "error_messages": {

                    "required": "Please enter your email address.",

                    "blank": "Email address cannot be blank.",

                    "invalid": (
                        "Please provide a valid email address "
                        "(e.g., name@example.com)."
                    ),

                }

            },

            "subject": {

                "error_messages": {

                    "required": "Please provide a subject for your message.",

                    "blank": "Subject cannot be blank.",

                }

            },

            "message": {

                "error_messages": {

                    "required": "Please type a message before sending.",

                    "blank": "Message cannot be blank.",

                }

            },

        }


    def validate_full_name(

        self,

        value

    ):

        value = value.strip()

        if not value:

            raise serializers.ValidationError(

                "Full name cannot consist only of spaces."

            )

        if len(value) < 3:

            raise serializers.ValidationError(

                "Full name must be at least 3 characters long."

            )

        return value


    def validate_subject(

        self,

        value

    ):

        value = value.strip()

        if not value:

            raise serializers.ValidationError(

                "Subject cannot consist only of spaces."

            )

        if len(value) < 5:

            raise serializers.ValidationError(

                "Subject must be at least 5 characters long."

            )

        return value


    def validate_message(

        self,

        value

    ):

        value = value.strip()

        if not value:

            raise serializers.ValidationError(

                "Message cannot consist only of spaces."

            )

        if len(value) < 20:

            raise serializers.ValidationError(

                "Please provide a more descriptive message "
                "(minimum 20 characters)."

            )

        return value


    def validate_honeypot(

        self,

        value

    ):

        if value.strip():

            raise serializers.ValidationError(

                "Spam detected."

            )

        return value


    def validate(

        self,

        attrs

    ):

        # Normalize values

        attrs["full_name"] = attrs["full_name"].strip()

        attrs["email"] = attrs["email"].strip().lower()

        attrs["subject"] = attrs["subject"].strip()

        attrs["message"] = attrs["message"].strip()


        # Duplicate submission protection

        recent_messages = ContactMessage.objects.filter(

            email__iexact=attrs["email"],

            subject__iexact=attrs["subject"],

            message=attrs["message"],

            created_at__gte=(

                timezone.now() -

                timedelta(

                    minutes=5

                )

            )

        )


        if recent_messages.exists():

            raise serializers.ValidationError(

                {

                    "detail":

                    "Duplicate message detected. Please wait a few minutes before sending again."

                }

            )


        return attrs
