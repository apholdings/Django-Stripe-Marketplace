from django.contrib import admin
from .models import UserLibrary, User
# Register your models here.

admin.site.register(User)
admin.site.register(UserLibrary)
