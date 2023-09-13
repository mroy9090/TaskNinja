from django.contrib import admin
from .models import Ipconfiguration
# Register your models here.

admin.site.register(Ipconfiguration)
# class IpconfigurationAdmin(admin.ModelAdmin):
#     list_display = ('id', 'version', 'interface_name','description', 'ip_address', 'net_mask')