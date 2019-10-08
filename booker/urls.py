from django.urls import path, re_path
from .views import RoomBookView, RoomListView

app_name = "articles"

urlpatterns = [
	# path('articles/', ArticleView.as_view()),
	# path('alluser/', AllUser.as_view()),
	# path('leaderboard/<string:matchname>/<string:time>', LeaderBoardView.as_view())
	# re_path(r'^leaderboard/', LeaderBoardView.as_view())
	path('bookroom/', RoomBookView.as_view()),
	path('roomlist/', RoomListView.as_view()),
	
]
