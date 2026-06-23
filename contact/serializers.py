from datetime import timedelta
from django.utils import timezone
from rest_framework import serializers
from .models import ContactMessage

SPAM_PATTERNS = [
    "bitcoin", "casino", "forex", "loan", "viagra", "seo", "backlinks",
    "crypto", "earn money", "work from home", "telegram", "whatsapp group",
    "investment opportunity", "click here", "free money",
]

class ContactMessageSerializer(serializers.ModelSerializer):
    # Virtual field for bot trapping; doesn't need to exist in the DB model
    honeypot = serializers.CharField(required=False, write_only=True, allow_blank=True)

    class Meta:
        model = ContactMessage
        fields = "__all__"
        read_only_fields = ("id", "is_read", "created_at")
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
                    "invalid": "Please provide a valid email address (e.g., name@example.com).",
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

    def validate_full_name(self, value):
        value = value.strip()
        if len(value) < 3:
            raise serializers.ValidationError("Full name must be at least 3 characters long.")
        return value

    def validate_subject(self, value):
        value = value.strip()
        if len(value) < 5:
            raise serializers.ValidationError("Subject must be at least 5 characters long.")
        return value

    def validate_message(self, value):
        value = value.strip()
        if len(value) < 20:
            raise serializers.ValidationError(
                "Please provide a more descriptive message (minimum 20 characters)."
            )
        return value

    def validate_honeypot(self, value):
        if value and value.strip():
            raise serializers.ValidationError("Spam detected.")
        return value

    def validate(self, attrs):
        # 1. Trapped by honeypot (if it was included in the payload but skipped field validation)
        if attrs.get("honeypot"):
            raise serializers.ValidationError({"detail": "Spam detected."})

        # 2. Normalize values before saving
        attrs["full_name"] = attrs.get("full_name", "").strip()
        attrs["email"] = attrs.get("email", "").strip().lower()
        attrs["subject"] = attrs.get("subject", "").strip()
        attrs["message"] = attrs.get("message", "").strip()

        # 3. Spam pattern check (Cross-field validation)
        combined_text = f"{attrs['subject']} {attrs['message']}".lower()
        if any(pattern in combined_text for pattern in SPAM_PATTERNS):
            raise serializers.ValidationError(
                {"message": "Your message appears to contain spam or promotional content."}
            )

        # 4. Duplicate submission protection
        cooldown_time = timezone.now() - timedelta(minutes=5)
        recent_messages = ContactMessage.objects.filter(
            email__iexact=attrs["email"],
            subject__iexact=attrs["subject"],
            message=attrs["message"],
            created_at__gte=cooldown_time
        )

        if recent_messages.exists():
            raise serializers.ValidationError(
                {"detail": "Duplicate message detected. Please wait a few minutes before sending again."}
            )

        return attrs