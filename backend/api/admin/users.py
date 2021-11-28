from django.contrib.admin import register, ModelAdmin
from ..models import Users


@register(Users)
class UsersAdminForm(ModelAdmin):
    list_display = ('username', 'email', 'password')
    list_display_links = ('username', 'email', 'password')
    search_fields = ('username', 'email')
