from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken.views import obtain_auth_token

from .views import BucketlistView, BucketlistDetailsView, ItemView, ItemsDetailsView, UserView, UserDetailsView

urlpatterns = {
    url(r'^accounts/', include('rest_registration.api.urls')),
    url(r'^bucketlists/$', BucketlistView.as_view(), name="create"),
    url(r'^bucketlists/(?P<pk>[0-9]+)/$', BucketlistDetailsView.as_view(), name="details"),
    url(r'^bucketlists/(?P<pk>[0-9]+)/items/$', ItemView.as_view(), name="create-item"),
    url(r'^bucketlists/(?P<pk>[0-9]+)/items/(?P<id>[0-9]+)$', ItemsDetailsView.as_view(), name="items"),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetailsView.as_view(), name="user-details"),
    url(r'^get-token/$', obtain_auth_token),
    url(r'^docs/', include('rest_framework_docs.urls'))
}

urlpatterns = format_suffix_patterns(urlpatterns)