from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('dashboard/', views.home, name='dashboard'),
    path('dashboard/ip/', views.ip, name='ip'),
    path('dashboard/bgp_configuration/', views.bgp, name='bgp_configuration'),
    path('dashboard/delete/<int:id>/', views.delete_data, name='delete_data'),

]
