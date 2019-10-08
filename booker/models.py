from django.db import models

# Create your models here.
class MeetingRoom(models.Model):
	room_name = models.CharField(max_length=200)
	occupied = models.BooleanField(default=False)

	def __str__(self):
		return self.room_name


class MeetingRoomLog(models.Model):
	room = models.ForeignKey('MeetingRoom', on_delete=models.CASCADE)
	booked_time = models.DateTimeField(auto_now_add=True)
	scheduled_time = models.CharField(max_length=200,default='')

	def __str__(self):
		return self.room.room_name

