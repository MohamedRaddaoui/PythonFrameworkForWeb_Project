from django.contrib import admin
from .models import *
from django.utils import timezone

# Register your models here.
class ConferenceDateFilter(admin.SimpleListFilter):
    title = 'Conference Date'
    parameter_name = 'conference_date'
    def lookups(self, request, model_admin):
        return (
            ('past', "Past Conferences"), 
            ('today', "Today Conferences"), 
            ('upcoming', "Upcoming Conferences")
        )
    def queryset(self, request, queryset):
        today = timezone.now().date()
        if self.value() == 'past':
            return queryset.filter(start_date__lt=today)
        if self.value() == 'today':
            return queryset.filter(start_date=today)
        if self.value() == 'upcoming':
            return queryset.filter(start_date__gt=today)
        return queryset

class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'start_date', 'end_date', 'location', 'price')
    ordering = ('title', 'start_date')
    search_fields = ('title', 'location')
    list_filter = ('location',ConferenceDateFilter)
    autocomplete_fields = ('category',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')

admin.site.register(Conference, ConferenceAdmin)
admin.site.register(Category, CategoryAdmin)