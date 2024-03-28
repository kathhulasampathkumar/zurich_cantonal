from django.urls import path, include
from fundtransfer import views

urlpatterns = [
    path('index', views.index, name='index'),            #default index page url      
    path('', views.home, name='home'),            #default index page url      
    path('getUserData', views.getUserData, name='getUserData'),            #default index page url      
]
# handler404 ='certificate_module.views.error_404'
