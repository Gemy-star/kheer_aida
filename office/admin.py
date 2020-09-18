from django.contrib import admin
from . import models

admin.site.register(models.RequestHelp)
admin.site.register(models.RequestConfirm)
admin.site.register(models.Donation)
