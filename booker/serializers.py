from rest_framework import serializers


class RoomSerializer(serializers.Serializer):
	room_name = serializers.CharField(max_length=200)

class RoomBookedSerializer(serializers.Serializer):
	room_name = serializers.CharField(max_length=200)
	scheduled_time = serializers.CharField(max_length=200)

