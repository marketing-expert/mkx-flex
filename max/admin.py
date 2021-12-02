# flex.admin.py

from django.contrib import admin

from max.models import Souscriber
from utils.export_data import export_to_csv


@admin.register(Souscriber)
class VisitorsAdmin(admin.ModelAdmin):
    model = Souscriber
    date_hierarchy = 'created_at'

    fieldsets = (
        (
            'Information client',
            {'fields':
                (   
                    ('gender', 'name'), ('faculte'),
                    'number_kit',
                    ('phone_one', 'phone_two'), 'amount',
                    (
                        'is_pack_easy', 'is_pack_gold', 'is_pack_fun',
                        'is_pack_phoenix', 'is_pack_silver'
                    )
                ),
            }
        ),
    )

    list_display = [
        "id", "get_client_name", "get_client_phone",
        'number_kit', 'is_pack_easy', 'is_pack_gold',
        'is_pack_fun', 'is_pack_phoenix', 'is_pack_silver',
        "created_at",
    ]
    list_display_links = [
        'get_client_name',
    ]
    list_filter = [
        'is_pack_easy', 'is_pack_gold', 'is_pack_fun',
        'is_pack_phoenix', 'is_pack_silver',
        "phone_one",
    ]
    list_per_page = 10
    ordering = ['-created_at']
    actions = [export_to_csv]
    search_fields = ['get_client_name', 'phone_one', 'phone_two']

    @admin.display(description='Nom & prénom')
    def full_name(self, obj):
        return f"{obj.gender} {obj.name}"
