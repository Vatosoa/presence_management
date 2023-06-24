from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static 
#from useregistration import urls as userurls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('useregistration.urls')), # ou  path('', include(userurls)), 
]

urlpatterns = urlpatterns+static(settings.MEDIA_URL,
                                 document_root=settings.MEDIA_ROOT)