from django.conf.urls import include, url


urlpatterns = [
    url(r'^', include('testphoto.photo.urls')), ]
