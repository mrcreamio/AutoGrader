from django.conf.urls import url

from . import views

# from django.contrib.auth import views as auth_views
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^login/$',views.login,name='login'),
    url(r'^teacher_index/$',views.teacher_index,name='teacher_index'),
    url(r'^teacher_portal/assignment_upload/$',views.assignment_upload,name='assignment_upload'),
    url(r'^teacher_portal/$',views.teacher_portal,name='teacher_portal'),
    url(r'^api/$', views.api, name='api'),
    url(r'^login/check_login/student_portal/assignment_download/assignments/pdf/(?P<slug>[^/]+)', views.assignment_download, name='assignment_download'),
    url(r'^login/check_login/student_portal/assignments/pdf/$', views.assignment_download, name='assignment_download'),
    url(r'^login/check_login/student_portal/assignment_download/$',views.assignment_download,name='assignment_download'),

    url(r'^teacher_index/teacher_login$',views.teacher_login,name='teacher_login'),
    url(r'^teacher_index/teacher_signup$',views.teacher_signup,name='teacher_signup'),
    url(r'^teacher_index/teacher_login_l$',views.teacher_login_l,name='teacher_login_l'),
    # url(r'^teacher_index/teacher_login/assignment_upload/$',views.assignment_upload,name='assignment_upload'),
    

    # url(r'^emp_detail/(?P<user_name>\w+)/(?P<mobile_number>\d{10,18})/$', views.emp_detail, name='emp_detail'),

    url(r'^login/check_login$',views.check_login,name='check_login'),
    url(r'^login/check_login/student_portal/$',views.registered_course,name='registered_course'),
    url(r'^signup/add_signup$',views.add_signup,name='add_signup'),
    url(r'^login/check_login/student_portal/marks/$',views.marks,name='marks'),
]
