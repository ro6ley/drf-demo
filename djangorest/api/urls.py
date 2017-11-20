from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken.views import obtain_auth_token

from .views import CreateView, DetailsView, CreateItemView, ItemsView

urlpatterns = {
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^bucketlists/$', CreateView.as_view(), name="create"),
    url(r'^bucketlists/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
    url(r'^bucketlists/(?P<pk>[0-9]+)/items/$', CreateItemView.as_view(), name="create-item"),
    url(r'^bucketlists/(?P<pk>[0-9]+)/items/(?P<id>[0-9]+)$', ItemsView.as_view(), name="items"),
    url(r'^get-token/$', obtain_auth_token),
    url(r'^docs/', include('rest_framework_docs.urls')),
}

urlpatterns = format_suffix_patterns(urlpatterns)