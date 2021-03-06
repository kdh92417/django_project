from django.contrib import admin
from .models        import Account

class AccountAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'password', 'email', 'created_at', 'updated_at')

admin.site.register(Account, AccountAdmin)
