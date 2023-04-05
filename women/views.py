from django.forms import model_to_dict
from django.shortcuts import redirect
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from women.models import Woman
from women.serializers import WomanSerializer


def index(request):
    return redirect('women')


# class WomanView(ListAPIView):
#     queryset = Woman.objects.all()
#     serializer_class = WomanSerializer


class WomanView(APIView):
    def get(self, request):
        women = Woman.objects.all().values()
        return Response({'posts': list(women)})

    def post(self, request):
        post = Woman.objects.create(
            name=request.data['name'],
            content=request.data['content'],
            categories_id=request.data['categories'])
        return Response({'post': model_to_dict(post)})


class WomanRetrieveUpdateView(APIView):
    def patch(self, request, pk):
        Woman.objects.filter(id=pk).update(
            content=request.data['content']
        )
        return Response({'status': 'OK'})

    def delete(self, request, pk):
        Woman.objects.filter(id=pk).delete()
        return Response({'status': 'OK'})
