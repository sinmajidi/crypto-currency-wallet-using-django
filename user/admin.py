from django.contrib import admin
from .models import User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','email','is_enable','is_confrimed','create_time','last_login','public_address','asset','profit']

