import django_filters

from .models import Province, Destination


class NullFilter(django_filters.BooleanFilter):
	"""Filter on a field set as null or not."""
	
	def filter(self, qs, value):
		if value is not None:
			return qs.filter(**{'{}__isnull'.format(self.name): value})
		return qs


class ProvinceFilter(django_filters.FilterSet):
	
	class Meta:
		model = Province
		fields = ('island',)
				

class DestinationFilter(django_filters.FilterSet):
	
	class Meta:
		model = Destination
		fields = ('province_name', )

