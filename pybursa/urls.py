from django.conf.urls import include, url, patterns
from django.contrib import admin
from pybursa import views

urlpatterns =  patterns('',
    # Examples:
    url(r'^$', views.show_index, name='index_pybursa'),
    url(r'^contacts/', views.contacts, name='contacts_pybursa'),
    url(r'^students/$', views.show_students, name='student_list'),
    url(r'^students/(?P<id>\d+)/$', views.show_student, name = 'student_detail'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^quadratic/', include('quadratic.urls', namespace = "quadratic")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^courses/(?P<id>\d+)/$', views.show_course, name = 'course'),
)
