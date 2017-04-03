from django.contrib import admin

# Register your models here.
from .models import CloudData

#admin.site.register(Post)

@admin.register(CloudData)
class CloudDataAdmin(admin.ModelAdmin):
    list_display  = ('location', 'bin_id', 'gw_id', 'time_stamp')
    list_filter  = ('location', 'bin_id')
