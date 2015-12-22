from django.contrib.auth import get_user_model

from rest_framework import authentication, permissions, viewsets, filters

from .forms import DestinationFilter, ProvinceFilter
from .models import Province, Destination
from .serializers import ProvinceSerializer, DestinationSerializer


class DefaultsMixin(object):
	"""Default settings for view authentication, permissions,
	filtering and pagination"""
	
	authentication_classes = (
	    authentication.BasicAuthentication,
	    authentication.TokenAuthentication,
	    authentication.SessionAuthentication
	)
	
	permission_classes =(
	    permissions.IsAuthenticatedOrReadOnly,
	)
	
	paginate_by = 25
	paginate_by_param = 'page_size'
	max_paginate_by = 100
	
	filter_backends = (
	    filters.DjangoFilterBackend,
	    filters.SearchFilter,
	    filters.OrderingFilter,
	)


class ProvinceViewSet(DefaultsMixin, viewsets.ModelViewSet):
	queryset = Province.objects.all()
	serializer_class = ProvinceSerializer
	filter_class = ProvinceFilter
	search_fileds = ('name',)
	ordering_fields = ('name', 'island')
	
	
	
class DestinationViewSet(DefaultsMixin, viewsets.ModelViewSet):
	"""API endpoint for listing and creating Destinations."""
	
	queryset = Destination.objects.all()
	serializer_class = DestinationSerializer
	filter_class = DestinationFilter
	search_fileds = ('name', )
	ordering_fields = ('name', 'province_name', )
	
