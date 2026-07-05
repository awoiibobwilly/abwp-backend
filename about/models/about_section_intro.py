from django.db import models


class AboutSectionIntro(models.Model):
    WHO_I_AM = "who_i_am"
    PROFESSIONAL_DNA = "professional_dna"
    CORE_VALUES = "core_values"
    SELECTED_ACHIEVEMENTS = "selected_achievements"
    CREDENTIALS = "credentials"
    SKILLS = "skills"

    SECTION_CHOICES = [
        (WHO_I_AM, "Who I Am"),
        (PROFESSIONAL_DNA, "Professional DNA"),
        (CORE_VALUES, "Core Values"),
        (SELECTED_ACHIEVEMENTS, "Selected Achievements"),
        (CREDENTIALS, "Credentials"),
        (SKILLS, "Skills & Tools"),
    ]

    section_key = models.CharField(
        max_length=50,
        choices=SECTION_CHOICES,
        unique=True,
    )
    eyebrow = models.CharField(max_length=120)
    title = models.CharField(max_length=255)
    intro = models.TextField()
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["section_key"]
        verbose_name = "About Section Intro"
        verbose_name_plural = "About Section Intros"

    def __str__(self):
        return f"{self.get_section_key_display()} Intro"