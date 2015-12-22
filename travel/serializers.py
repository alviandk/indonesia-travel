from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from rest_framework.reverse import reverse

from travel.models import Province, Destination

class ProvinceSerializer(serializers.ModelSerializer):	
    links = serializers.SerializerMethodField()
	
    class Meta:
		model = Province
		fields = ('name', 'short_description', 'island', 'url', 'links')
		
    def get_links(self, obj):
		request = self.context['request']
		return {
		    'self': reverse('province-detail',
		        kwargs={'pk': obj.pk}, request=request),
		    
		}


class DestinationSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()

    class Meta:
		model = Destination
		fields = ('name', 'short_description', 'province_name', 
					'latitude', 'longitude','url', 'links')
		
    def get_links(self, obj):
		request = self.context['request']
		links = {
		    'self': reverse('destination-detail',
		        kwargs={'pk': obj.pk}, request=request),
		    'province': None,		    
		}
		if obj.province_name_id:
			links['province'] = reverse('province-detail',
			    kwargs={'pk': obj.province_name.pk}, request=request)
		
		return links

