from rest_framework import serializers
from .models import ContactMessage


class ContactMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactMessage
        fields = "__all__"
        read_only_fields = (
            "id",
            "is_read",
            "created_at",
        )
        # Override the built-in field validation messages for native UI text
        extra_kwargs = {
            "full_name": {
                "error_messages": {
                    "required": "Please enter your full name.",
                    "blank": "Full name cannot be blank."
                }
            },
            "email": {
                "error_messages": {
                    "required": "Please enter your email address.",
                    "blank": "Email address cannot be blank.",
                    "invalid": "Please provide a valid email address (e.g., name@example.com)."
                }
            },
            "subject": {
                "error_messages": {
                    "required": "Please provide a subject for your message.",
                    "blank": "Subject cannot be blank."
                }
            },
            "message": {
                "error_messages": {
                    "required": "Please type a message before sending.",
                    "blank": "Message cannot be blank."
                }
            }
        }

    def validate_full_name(self, value):
        cleaned_value = value.strip()
        if not cleaned_value:
            raise serializers.ValidationError("Full name cannot consist of only spaces.")
        if len(cleaned_value) < 3:
            raise serializers.ValidationError("Full name must be at least 3 characters long.")
        return cleaned_value

    def validate_subject(self, value):
        cleaned_value = value.strip()
        if not cleaned_value:
            raise serializers.ValidationError("Subject cannot consist of only spaces.")
        if len(cleaned_value) < 5:
            raise serializers.ValidationError("Subject must be at least 5 characters long.")
        return cleaned_value

    def validate_message(self, value):
        cleaned_value = value.strip()
        if not cleaned_value:
            raise serializers.ValidationError("Message cannot consist of only spaces.")
        if len(cleaned_value) < 20:
            raise serializers.ValidationError("Please provide a more descriptive message (at least 20 characters).")
        return cleaned_value

    def validate_honeypot(

        self,

        value

    ):

        if value.strip():

            raise serializers.ValidationError(

                "Spam detected."

            )

        return value

    def validate(self, attrs):
        # Safely normalize values using .get() to prevent server-crashing KeyErrors
        if "full_name" in attrs:
            attrs["full_name"] = attrs["full_name"].strip()
            
        if "email" in attrs:
            attrs["email"] = attrs["email"].strip().lower()
            
        if "subject" in attrs:
            attrs["subject"] = attrs["subject"].strip()
            
        if "message" in attrs:
            attrs["message"] = attrs["message"].strip()

        if "validate_honeypot" in attrs:
            attrs["validate_honeypot"] = attrs["validate_honeypot"].strip()

        return attrs