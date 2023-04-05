from rest_framework.serializers import ModelSerializer
from women.models import Woman


class WomanSerializer(ModelSerializer):
    class Meta:
        model = Woman
        fields = ['name', 'categories']
