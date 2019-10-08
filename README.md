# meetingbooker

## api routes
  - baseurl/api/bookroom/?time="YOURTIME"
  - baseurl/api/roomlist/
  
## prerequisites installation

     pip3 install -r requirements.txt
          
     
## Running the server

     python manage.py migrate
     python manage.py makemigrations
     python manage.py runserver
     
## Creating models:
 
     python manage.py shell
     from booker.models import MeetingRoom
     room = MeetingRoom.objects.create(room_name="first conference room")


   
     
## sample endpoints at very embrionic stage

![Screenshot from 2019-10-08 23-47-33](https://user-images.githubusercontent.com/9798362/66422058-9d496300-ea26-11e9-9b42-fe2f05b612f4.png)
![Screenshot from 2019-10-08 23-47-49](https://user-images.githubusercontent.com/9798362/66422061-9f132680-ea26-11e9-897c-97d7a566944f.png)
