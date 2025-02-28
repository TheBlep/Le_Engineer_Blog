from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]

# from django.urls import path
# from . import views
	
# urlpatterns = [
# 	path("", views.index, name="index")
# ]

