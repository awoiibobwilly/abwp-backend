from django.db import models


class WhoIAm(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    icon = models.CharField(
        max_length=100,
        blank=True,
        default="",
        help_text="Frontend icon key, e.g. FaUserDoctor",
    )

    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Who I Am Item"
        verbose_name_plural = "Who I Am Items"
        ordering = ["display_order", "id"]

    def __str__(self):
        return self.title