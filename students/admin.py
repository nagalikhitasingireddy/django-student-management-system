from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "roll_number", "course", "marks"]
    search_fields = ["name", "roll_number"]
    list_filter = ["course"]


admin.site.register(Student, StudentAdmin)