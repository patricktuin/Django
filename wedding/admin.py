from django.contrib import admin

# Register your models here.
from wedding.models import Invitee, Invitee_extra

class ChoiceInline(admin.TabularInline):
    model = Invitee_extra
    extra = 1

class WeddingAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['invitee']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('invitee', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['invitee']

admin.site.register(Invitee, WeddingAdmin)
