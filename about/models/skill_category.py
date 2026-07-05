from django.db import models


class SkillCategory(models.Model):
    title = models.CharField(max_length=150)

    skills = models.JSONField(
        default=list,
        blank=True,
        help_text=(
            "List of skills under this category. Example: "
            '["Python", "Django", "React"]'
        ),
    )

    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Skill Category"
        verbose_name_plural = "Skill Categories"
        ordering = ["display_order", "id"]

    def __str__(self):
        return self.title