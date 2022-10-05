from django.urls import path

from . import views
app_name='newapp'
urlpatterns = [
    path('', views.demo, name='demo'),
    path('demo/<int:movie_id>/', views.detail, name='detail'),
    path('add/',views.add,name='add'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]
