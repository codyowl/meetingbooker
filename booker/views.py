from django.shortcuts import render
from rest_framework.views import APIView
from booker.models import MeetingRoom, MeetingRoomLog
from django.http import HttpResponse
from rest_framework.response import Response
from booker.serializers import RoomSerializer, RoomBookedSerializer


# Create your views here.
class RoomBookView(APIView):
	def get(self, request):
		time = request.GET.get('time', '')
		room = [r for r in MeetingRoom.objects.all() if r.occupied==False][0]
		m = MeetingRoomLog()
		r = room
		m.room = room
		m.room.occupied = True
		m.scheduled_time = time
		m.save() 
		r.occupied = True
		r.save()
		serializer_dict = {
			'room_name' : m.room.room_name,
			'scheduled_time' : m.scheduled_time
		}
		serializer = RoomBookedSerializer(serializer_dict)
		
		return Response({"ConferenceroomBooked":serializer.data})


class RoomListView(APIView):
	def get(self, request):
		rooms = MeetingRoom.objects.filter(occupied=False)
		if not rooms:
			return Response({"Result": "All rooms are occupied"})
		else:
			serializer = RoomSerializer(rooms, many=True) #many for too many thigs in a list
		return Response({"roomList":serializer.data})
	

			