from django.conf.urls import url
from django.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from civic_sandbox import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'slides', views.SlideSet)
router.register(r'foundations', views.FoundationSet)
router.register(r'packages', views.PackagesSet)

# https://github.com/encode/django-rest-framework/issues/1337
router.include_format_suffixes = False

urlpatterns = [
    url(r'^slides/poi/', views.poi),
    url(r'^foundations/shaking/', views.shaking),
    url(r'^foundations/liquefaction/', views.liquefaction),
    url(r'^foundations/landslide/', views.landslide),
    url(r'^foundations/censusresponse/', views.censusresponse),
    url(r'^packages/', include(router.urls)),
    url(r'^package_info/', views.packages_view, name='package_info')
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
