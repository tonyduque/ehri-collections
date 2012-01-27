from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_detail
from django.contrib.auth.decorators import login_required
from ehriportal.portal import views, models

from haystack.views import FacetedSearchView
from haystack.forms import FacetedSearchForm
from haystack.query import SearchQuerySet

sqs = SearchQuerySet().models(models.Repository).facet('country')

infodict = dict(
        queryset=models.Repository.objects.all()
)

urlpatterns = patterns('',
    url(r'^/?$', FacetedSearchView(
        form_class=FacetedSearchForm, searchqueryset=sqs,
        template="portal/repository_search.html"), name='repo_search'),
    url(r'^(?P<slug>[-\w]+)/?$', object_detail, infodict, name='repo_detail'),
)
