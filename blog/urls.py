
from django.urls import path
from blog.views import home,log_in,report,contacts,donate,signin,about,donor,Logout,money
urlpatterns = [
  
    path("", home,name="index"),
    path("login", log_in,name="login"),
    path("report", report,name="report"),
    path("contacts", contacts,name="contacts"),
    path("donate", donate,name="donate"),
    path("signin", signin,name="signin"),
    path("about", about,name="about"),
    path("donor", donor,name="donor"),
    path("logout",Logout,name="logout"),
    path("money",money,name="money"),
  
]
