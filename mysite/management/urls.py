from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^login/$',views.user_login,name='login'),
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'^record/(?P<type_or_id>\w*)\/*',views.get_records,name='get_records'),

]