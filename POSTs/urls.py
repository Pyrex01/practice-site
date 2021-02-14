from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path("poster",views.poster,name="poster"),
    path("adUp",views.post,name="post")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)