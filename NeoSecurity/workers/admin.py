from django.contrib import admin
from .models import Grade, Group, Worker, Document, WorkerGroup


@admin.register(Grade)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Group)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Worker)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['username']


@admin.register(Document)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(WorkerGroup)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['id']
