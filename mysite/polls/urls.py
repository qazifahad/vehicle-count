from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from polls import views
from django.conf.urls.static import static
urlpatterns = [
   path("",views.index,name='home')
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)