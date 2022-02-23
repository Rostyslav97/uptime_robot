from enum import Enum
from django.db import models


class Website(models.Model):
    url = models.TextField()
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name}"


class ReportStatuses(Enum):
    AVAILABLE = "Available"
    NOTAVAILABLE = "NotAvailable"
    BLOCKED = "Blocked"
    HACKED = "Hacked"

    @classmethod
    def choices(cls) -> list[tuple]:
        return [(a.value, a.value) for a in cls]


class Report(models.Model):
    site = models.ForeignKey(
        "Website", related_name="reports", on_delete=models.DO_NOTHING
    )
    status = models.CharField(max_length=15, choices=ReportStatuses.choices())

    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.site}"