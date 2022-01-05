from django.contrib import admin
from .models import Raid, Boss

# Register your models here.

@admin.register(Raid)
class RaidAdmin(admin.ModelAdmin):
    model = Raid
    list_display = ['name']

@admin.register(Boss)
class BossAdmin(admin.ModelAdmin):
    model = Boss
    list_display = ['name', 'raid_wing', 'id']