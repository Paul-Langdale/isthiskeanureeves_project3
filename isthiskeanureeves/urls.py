from django.conf.urls import url
from isthiskeanureeves import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'home/$', views.home, name='home'),
	url(r'kea-new/$', views.keanew, name='keanew'),
	url(r'about/$', views.about, name='about'),
        url(r'^register/$',views.register, name='register'),
	
	url(r'kea-not-him/$', views.keanothim, name='keanothim'),
	url(r'login/$', views.login, name='login'),
        url(r'^restricted/', views.restricted, name='restricted'),
	url(r'upload/$', views.upload, name='upload'),
	url(r'^post/(?P<post_title_slug>[\w\-]+)/$',
        views.post, name='post'),
]
