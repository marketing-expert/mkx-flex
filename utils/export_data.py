# utils.export_data.py

import csv
from datetime import datetime
from django.contrib import admin
from django.http import HttpResponse


@admin.display(description="Exporter au format CSV")
def export_to_csv(modeladmin, request, queryset):
    option = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = "attachment; filename={}.csv".format(option.verbose_name)

    writer = csv.writer(response)
    fields = [
        field for field in option.get_fields()
    ]

    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime):
                value = value.strftime("%d/%m/%Y")
            data_row.append(value)
        writer.writerow(data_row)

    return response
