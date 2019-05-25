from django.contrib import admin

class UserAdmin(admin.ModelAdmin):
    exclude = ('last_login', 'groups', 'user_permissions', 'is_superuser', \
        'date_joined', 'email', 'access_token', 'token_expire_time', 'is_staff',\
        'is_active', 'is_password_hashed')
