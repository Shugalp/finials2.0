from django.contrib import admin
from resume import models

# Register your models here.

@admin.register(
    models.Letter,
)


class Admin(admin.ModelAdmin):
    pass


