from django.contrib import admin

# Register your models here.
from wedding.models import Invitee, Invitee_extra

class ChoiceInline(admin.TabularInline):
    model = Invitee_extra
    extra = 1

class WeddingAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['party_name']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('party_name', 'created_at', 'updated_at')
    list_filter = ['created_at']
    search_fields = ['party_name']

admin.site.register(Invitee, WeddingAdmin)
