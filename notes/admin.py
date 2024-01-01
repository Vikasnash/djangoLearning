from django.contrib import admin

from . import models


# Register your models here.
class NotesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    pass  # dont want to app additional configuration


admin.site.register(models.Notes, NotesAdmin)
# admin.site.register()   ## we should provide arguments here
