from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from core import views as core_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', core_views.home, name='home'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, 
        {'next_page': '/'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^profile/$', core_views.edit_profile, name='edit_profile'),
]
