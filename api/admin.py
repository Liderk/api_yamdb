from django.contrib import admin
from .models import User, Categories, Genres, Titles, Review, Comments

class UserAdmin(admin.ModelAdmin):
    # перечисляем поля, которые должны отображаться в админке
    list_display = ("pk", "username", "role", "is_superuser")
    # добавляем интерфейс для поиска по имени пользователя
    search_fields = ("username",)
    # добавляем возможность фильтрации по ролям
    list_filter = ("role",)
    # это свойство сработает для всех колонок: где пусто - там будет эта строка
    empty_value_display = '-пусто-'

admin.site.register(User, UserAdmin)
