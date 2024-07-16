from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>/view_resume",views.view_resume,name="view_resume"),
    path("<int:id>/download",views.download,name="download"),
    path("register",views.register,name="register"),
    path("login",views.userlogin,name="login"),
    path("logout",views.logout,name="logout"),
    path("resume_list",views.resume_list,name="resume_list")
]