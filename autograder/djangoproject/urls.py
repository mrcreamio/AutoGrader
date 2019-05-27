from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    url(r'^home/',include('home.urls')),
    url(r'^signup/',include('home.urls')),
    url(r'^login/',include('home.urls')),
    # url(r'^teacher_portal/assignment_upload/',include('home.urls')),
    # url(r'^teacher_index/teacher_login/assignment_upload$/(?P<course_name>\w+)/(?P<course_code>\d+)/',include('home.urls')),
    url(r'^teacher_portal/',include('home.urls')),
    url(r'^teacher_portal/assignment_upload/(?P<course_name>\w+)',include('home.urls')),
    url(r'^assignments/assignments/',include('home.urls'))
    
    
]

# if settings.DEBUG:  # remember to set 'DEBUG = True' in settings.py
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)