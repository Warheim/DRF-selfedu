from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from women.models import Woman
from women.serializers import WomanSerializer


def index(request):
    return redirect('women')


class WomanView(APIView):
    def get(self, request):
        women = Woman.objects.all().values()
        return Response({'posts': WomanSerializer(women, many=True).data})

    def post(self, request):
        serializer = WomanSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            return Response({'error': 'Method PUT not allowed'})
        try:
            instance = Woman.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exist'})

        serializer = WomanSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            return Response({'error': 'Method DELETE is not allowed'})
        try:
            Woman.objects.get(pk=pk).delete()
        except:
            return Response({'error': 'Object does not exist'})
        return Response({'delete': f'Object {pk} deleted'})
