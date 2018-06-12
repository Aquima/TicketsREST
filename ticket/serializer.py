from ticket.models import Ticket
from rest_framework import serializers
class TicketSerializer(serializers.Serializer):
   # id = serializers.ReadOnlyField()  # read only
    code = serializers.CharField()
    title = serializers.CharField()
    date = serializers.DateField(format="%Y-%m-%d %H:%M:%S")
    startTime = serializers.TimeField(format="%H:%M:%S")
    endTime = serializers.TimeField(format="%H:%M:%S")
    address = serializers.CharField()
    detail = serializers.CharField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    modify_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    url_img = serializers.URLField()

    def create(self, validated_data):
        instance = Ticket()
        return self.update(instance, validated_data)

    def update(self, validated_data):
        instance = Ticket()
        instance.code = validated_data.get('code')
        instance.title = validated_data.get('title')
        instance.date = validated_data.get('date')
        instance.startTime = validated_data.get('startTime')
        instance.endTime = validated_data.get('endTime')
        instance.address = validated_data.get('address')
        instance.detail = validated_data.get('detail')
        instance.created_at = validated_data.get('created_at')
        instance.modify_at = validated_data.get('modify_at')
        instance.url_img = validated_data.get('url_img')
        instance.save()
        return instance

