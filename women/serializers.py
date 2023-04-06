import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from women.models import Woman, Category


class WomanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Woman
        fields = ['id', 'name', 'content', 'is_published', 'categories']


"""Как работает ModelSerializer под капотом описано ниже"""
# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


# class WomanSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     categories_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Woman.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.content = validated_data.get('content', instance.content)
#         instance.time_create = validated_data.get('time_create', instance.time_create)
#         instance.time_update = validated_data.get('time_update', instance.time_update)
#         instance.is_published = validated_data.get('is_published', instance.is_published)
#         instance.categories_id = validated_data.get('categories_id', instance.categories_id)
#         instance.save()
#         return instance


# def encode():
#     model = WomenModel('Vova', 'Vova: Be rich')
#     model_serialized = WomanSerializer(model)
#     print(model_serialized.data, type(model_serialized.data), sep='\n')
#     json = JSONRenderer().render(model_serialized.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Vova","content":"Vova: Be rich"}')
#     data = JSONParser().parse(stream)
#     serializer = WomanSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
