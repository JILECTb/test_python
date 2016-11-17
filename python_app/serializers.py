from django.contrib.auth.models import User
from rest_framework import serializers
from python_app.models import Device, Reading
from datetime import datetime

# Добавить сущность пользователя и привязать к ней приборы учета:
# Я решил связать приборы учета с существующей сущностью авторизации пользователя auth.User

class UserSerializer(serializers.ModelSerializer):
    devices = serializers.PrimaryKeyRelatedField(many=True, queryset=Device.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username', 'devices')

class DeviceSerializer(serializers.ModelSerializer):
    readings = serializers.PrimaryKeyRelatedField(many=True, queryset=Reading.objects.all())
    user_id = serializers.ReadOnlyField(source='user_id.id')
    class Meta:
        model = Device
        fields = ('device_id', 'review_date', 'premises', 'user_id', 'service', 'readings')

class ReadingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reading
        fields = ('reading_id', 'device_id', 'value')

    # При передаче показаний необходимо проверять, чтобы передаваемое показание было не меньше предыдущего, а также, чтобы разница между переданным и предыдущим показанием не превышало значение 50.

    def validate(self, data):
        try:
            last_reading = Reading.objects.filter(device_id=data['device_id']).order_by('-reading_id')[0:1].get()
            if (data['value'] < last_reading.value) or (data['value'] - last_reading.value >= 50):
                raise serializers.ValidationError("Reading could not be created with received data")
        except Reading.DoesNotExist:
            pass
        return data

    # Обновляем дату проверки прибора учета по которому были добавлены показания

    def create(self, validated_data):
        try:
            updated_device = Device.objects.get(device_id=validated_data['device_id'].device_id)
            updated_device.review_date = datetime.now()
            updated_device.save()
        except Device.DoesNotExist:
            pass
        return Reading.objects.create(**validated_data)
