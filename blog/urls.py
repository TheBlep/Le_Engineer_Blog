from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
]

# from django.urls import path
# from . import views
	
# urlpatterns = [
# 	path("", views.index, name="index")
# ]

