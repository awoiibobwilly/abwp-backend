from django.db import models


class Statistic(

    models.Model

):

    title = models.CharField(

        max_length=100

    )

    value = models.PositiveIntegerField()

    suffix = models.CharField(

        max_length=10,

        blank=True,

        default=""

    )

    icon = models.CharField(

        max_length=50,

        blank=True

    )

    display_order = models.PositiveIntegerField(

        default=1

    )

    is_active = models.BooleanField(

        default=True

    )

    created_at = models.DateTimeField(

        auto_now_add=True

    )

    updated_at = models.DateTimeField(

        auto_now=True

    )


    class Meta:

        ordering = [

            "display_order"

        ]

        verbose_name = "Statistic"

        verbose_name_plural = "Statistics"


    def __str__(

        self

    ):

        return self.title
