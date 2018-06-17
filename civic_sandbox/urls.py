from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^slides/poi/', views.poi),
    url(r'^foundations/shaking/', views.shaking),
    url(r'^foundations/liquefaction/', views.liquefaction),
    url(r'^foundations/landslide/', views.landslide),
    url(r'^foundations/censusresponse/', views.censusresponse),
            
]
urlpatterns = format_suffix_patterns(urlpatterns)
