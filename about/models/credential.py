from django.db import models


class Credential(models.Model):
    EDUCATION = "education"
    CERTIFICATION = "certification"

    GROUP_CHOICES = [
        (EDUCATION, "Education"),
        (CERTIFICATION, "Certification"),
    ]

    group = models.CharField(
        max_length=30,
        choices=GROUP_CHOICES,
        default=EDUCATION,
    )

    title = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    period = models.CharField(
        max_length=100,
        blank=True,
        default="",
    )
    note = models.TextField(blank=True, default="")

    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Credential"
        verbose_name_plural = "Credentials"
        ordering = ["group", "display_order", "id"]

    def __str__(self):
        return f"{self.title} - {self.institution}"