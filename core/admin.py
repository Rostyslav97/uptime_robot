from django.contrib import admin
from core.models import Report, ReportStatuses, Website


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("site", "status", "created_at", "available")
    search_fields = ("site", "status", "created_at", "available")

    @admin.display(boolean=True)
    def available(self, obj):
        return obj.status == ReportStatuses.AVAILABLE.value

class ReportInline(admin.TabularInline):
    model = Report

@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    inlines = [ReportInline]