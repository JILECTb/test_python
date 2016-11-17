from django.contrib import admin
from python_app.models import Device, Reading

#В Django-админке необходимо предусмотреть добавление приборов учета, а также вывод переданных показаний.

class ReadingAdmin(admin.ModelAdmin):
    list_display = ('reading_id', 'device_id', 'value')
    raw_id_fields = ('device_id',)

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'review_date', 'premises', 'service')

admin.site.register(Device, DeviceAdmin)
admin.site.register(Reading, ReadingAdmin)
