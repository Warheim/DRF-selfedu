from django.shortcuts import redirect
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from women.models import Woman, Category
from women.serializers import WomanSerializer


def index(request):
    return redirect('women-list')


"""Как работают ViewSet'ы (заменяя ViewClass'ы), как работает экшн добавления пути к роутам (показывает categories)"""


#   Если тут убираем queryset, то добавляем имя в basename в роутер. А убираем мы его чтобы воспользоваться get_queryset
class WomanViewSet(ModelViewSet):
    # queryset = Woman.objects.all()
    serializer_class = WomanSerializer

    #   Это для получения определенных записей или срезов:

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Woman.objects.all()[:3]
        return Woman.objects.filter(pk=pk)

    #   Это для регистрации роута под categories, его раньше не было

    @action(methods=['get'], detail=True)
    def show_cats(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})


"""Как работают готовые View-классы (заменяя ApiView) из коробки но без ViewSet'ов описано ниже"""

# class WomanView(ListCreateAPIView):
#     queryset = Woman.objects.all()
#     serializer_class = WomanSerializer
#
#
# class WomanUpdate(UpdateAPIView):
#     queryset = Woman.objects.all()
#     serializer_class = WomanSerializer
#
#
# class WomanDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Woman.objects.all()
#     serializer_class = WomanSerializer


"""Как работает APIView (заменяя рукописные view) под капотом описано ниже"""

# class WomanView(APIView):
#     def get(self, request):
#         women = Woman.objects.all()
#         return Response({'posts': WomanSerializer(women, many=True).data})
#
#     def post(self, request):
#         serializer = WomanSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk')
#         if not pk:
#             return Response({'error': 'Method PUT not allowed'})
#         try:
#             instance = Woman.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Object does not exist'})
#
#         serializer = WomanSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk')
#         if not pk:
#             return Response({'error': 'Method DELETE is not allowed'})
#         try:
#             Woman.objects.get(pk=pk).delete()
#         except:
#             return Response({'error': 'Object does not exist'})
#         return Response({'delete': f'Object {pk} deleted'})
