from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from account.views import UserViewSet
from django.conf.urls.static import static
from django.conf import settings
from account import views

router = routers.SimpleRouter()
router.register(r'user',UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^register/$', views.CreateMemberView.as_view(),name='member'),
    url(r'^api_auth/', include('rest_framework.urls',namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
