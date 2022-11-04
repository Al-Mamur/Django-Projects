from django.urls import path
from myapp import views

app_name = "myapp"


urlpatterns = [

path('', views.IndexView.as_view(), name="index"),
path('musicain_details/<pk>/', views.MusicianDetails.as_view(), name='musicain_details'),
path('add_musician/', views.AddMusician.as_view(), name='add_musician'),
path('musicain_update/<pk>/', views.UpdateMusician.as_view(), name='musicain_update'),
path('musician_delete/<pk>/', views.DeleteMusician.as_view(), name='musician_delete')
]
