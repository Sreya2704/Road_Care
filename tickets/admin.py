from django.contrib import admin

# Register your models here.

from tickets.models import User

admin.site.register(User)