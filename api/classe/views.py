from rest_framework import generics
from django.shortcuts import get_object_or_404
from .serializers import ClasseSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from api.models import *
from django_filters import rest_framework as filters
from .filters import ClasseFilter


class ClasseViewSet(viewsets.ModelViewSet):
    serializer_class = ClasseSerializer
    queryset = Classe.objects.all()
    filterset_fields = ('nom', 'prix', 'matiere', 'niveau', 'dateDebut', 'dateFin', 'dateFinInscription')

    def list(self, request):
        queryset = Classe.objects.all()
        serializer = ClasseSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Classe.objects.all()
        classe = get_object_or_404(queryset, pk=pk)
        serializer = ClasseSerializer(classe)
        return Response(serializer.data)

    def create(self, request):
        serializer = ClasseSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Classe creee'})
        else:
            return Response(serializer.errors,
                            status=400)

    def update(self, request, pk=None):
        instance = Classe.objects.filter(idClass=pk).first()
        serializer = ClasseSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            print(serializer.errors)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        instance = Classe.objects.filter(idClass=pk).first()
        instance.delete()
        return Response("Classe bien supprime", status=201)


class ClasseListView(generics.ListAPIView):
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer
    paginate_by = 100
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('nom', 'prix')
    filterset_class = ClasseFilter