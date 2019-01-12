from rest_framework import generics
from django.shortcuts import get_object_or_404
from .serializers import ChapitreClasseSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from api.models import ChapitreClasse
from django_filters import rest_framework as filters
from .filters import ChapitreClasseFilter


class ChapitreClasseViewSet(viewsets.ModelViewSet):
    serializer_class = ChapitreClasseFilter
    queryset = ChapitreClasse.objects.all()
    filterset_fields = ('intitule', 'matiere')

    def list(self, request):
        queryset = ChapitreClasse.objects.all()
        serializer = ChapitreClasseSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = ChapitreClasse.objects.all()
        chapitre = get_object_or_404(queryset, pk=pk)
        serializer = ChapitreClasseSerializer(chapitre)
        return Response(serializer.data)

    def create(self, request):
        serializer = ChapitreClasseSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Chapitre creee'})
        else:
            return Response(serializer.errors,
                            status=400)

    def update(self, request, pk=None):
        instance = ChapitreClasse.objects.filter(id=pk).first()
        serializer = ChapitreClasseSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            print(serializer.errors)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        instance = ChapitreClasse.objects.filter(id=pk).first()
        instance.delete()
        return Response("Chapitre bien supprime", status=201)


class ChapitreClasseListView(generics.ListAPIView):
    queryset = ChapitreClasse.objects.all()
    serializer_class = ChapitreClasseSerializer
    paginate_by = 100
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('intitule', 'matiere')
    filterset_class = ChapitreClasseFilter