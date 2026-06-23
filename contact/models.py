from django.db import models


class ContactMessage(models.Model):

    full_name = models.CharField(
        max_length=150
    )

    email = models.EmailField()

    subject = models.CharField(
        max_length=255
    )

    message = models.TextField()

    honeypot = models.CharField( 
        max_length=100,
        blank=True, default="")

    is_read = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = ["-created_at"]

        verbose_name = "Contact Message"

        verbose_name_plural = "Contact Messages"

    def __str__(self):

        return f"{self.full_name} - {self.subject}"
