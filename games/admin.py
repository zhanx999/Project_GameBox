from django.contrib import admin

from .models import*
# Register your models here.

class ScreenshotInLine(admin.TabularInline):
    model = Screenshot
    extra= 1

class GameAdmin(admin.ModelAdmin):
    list_display = ('title','image','release_date')
    search_fields = ('title','genre','developer')
    ordering = ('title',)
    inlines = [ScreenshotInLine]

admin.site.register(Game,GameAdmin)
# admin.site.register(Screenshot)