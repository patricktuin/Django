from django.contrib import admin

# Register your models here.
from food.models import Dish, Ingredient

class ChoiceInline(admin.TabularInline):
    model = Ingredient
    extra = 1

class DishAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ('Servers how many people', {'fields': ['persons']}),
        ('Image link or url', {'fields': ['url']}),
        ('Preparation', {'fields': ['preparation']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name']

admin.site.register(Dish, DishAdmin)
