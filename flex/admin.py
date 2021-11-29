# flex.admin.py

from django.contrib import admin
from django.contrib.auth.models import Group

from flex.models import Visitor
from utils.export_data import export_to_csv


@admin.register(Visitor)
class VisitorsAdmin(admin.ModelAdmin):
    model = Visitor
    date_hierarchy = 'created_at'

    fieldsets = (
        (
            'Information visiteurs',
            {'fields':
                (
                    ('gender', 'name'),
                    ("email", 'phone')
                ),
            }
        ),
        (
            'Information sur la visite', {
                'classes': ('collapse',),
                'fields': (
                    "subject_visit",
                    ("hour_start_visit", "hour_end_visit"),
                )
            }
        ),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide', 'extrapretty'),
            'fields': ('email', 'is_staff', 'is_active',)
        }),
    )

    list_display = [
        "full_name", "email", "phone",
        "subject_visit", "created_at",
    ]
    list_display_links = [
        'full_name', 'email'
    ]
    list_filter = [
        "created_at",
        "subject_visit",
    ]
    list_per_page = 10
    ordering = ['-created_at']
    actions = [export_to_csv]
    readonly_fields = ['email', 'phone']
    search_fields = ["full_name", 'email']

    @admin.display(description='Nom & prénom')
    def full_name(self, obj):
        return f"{obj.gender} {obj.name}"


admin.site.unregister(Group)
