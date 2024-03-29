"""SWD_BACKEND_TEST URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from todolist.views import todolist_create, todolist_update, todolist_delete
from apis.views.schools import StudentSubjectsScoreAPIView, StudentSubjectsScoreDetailsAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apis.urls')),
    path('api/todolistcreate/', todolist_create, name='to do list create'),
    path('api/todolistupdate/', todolist_update, name='to do list update'),
    path('api/todolistdelete/', todolist_delete, name='to do list delete'),
    path('api/studentsubjectsscoreapiview/', StudentSubjectsScoreAPIView.as_view(), name='StudentSubjectsScoreAPIView'),
    path('api/studentsubjectsscoredetailsapiview/', StudentSubjectsScoreDetailsAPIView.as_view(), name='StudentSubjectsScoreDetailsAPIView'),

]
