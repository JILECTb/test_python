from django.db import models

SERVICES = (
    ('HOT_WATER', 'Горячая вода'),
    ('COLD_WATER', 'Холодная вода'),
    ('ELECTRICITY', 'Электричество'),
)

'''
Каждый прибор учета имеет следующие атрибуты:
a.	ID (целое)
b.	Дата поверки (дата и время)
c.	Помещение (строковое значение)
d.	Услуга (строковое значение) - возможные значения “горячая вода”, ”холодная вода”, “электричество”
'''

class Device(models.Model):
    device_id = models.AutoField(primary_key=True)
    review_date = models.DateTimeField()
    premises = models.CharField(max_length=100)
    service = models.CharField(max_length=100, choices=SERVICES)
    user_id = models.ForeignKey('auth.User', related_name='devices', on_delete=models.CASCADE)

'''
Каждое показание имеет следующие атрибуты:
a.	ID (целое)
b.	ID счетчика (целое)
c.	Величина (positive float)
'''

class Reading(models.Model):
    reading_id = models.AutoField(primary_key=True)
    device_id = models.ForeignKey(Device, related_name='readings', on_delete=models.CASCADE)
    value = models.DecimalField(default=0, max_digits=10, decimal_places=2)