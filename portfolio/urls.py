from django.contrib import admin
from django.urls import path
from portfolio import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    # path('blog/',views.handleblog,name='blog'),
    path('internshipdetails/',views.internshipdetails,name='internshipdetails'),
    path('project_portfolio/',views.project_portfolio,name='project_portfolio'),
    path('Resume_skills/',views.Resume_skills,name='Resume_skills'),
]
