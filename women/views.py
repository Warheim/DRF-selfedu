from django.shortcuts import redirect
from rest_framework.generics import ListAPIView
from women.models import Woman
from women.serializers import WomanSerializer


def index(request):
    return redirect('women')


class WomanView(ListAPIView):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer
