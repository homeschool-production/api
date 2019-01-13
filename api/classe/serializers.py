from rest_framework import serializers
from api.models import Classe, EnseigneAClasse


class ClasseSerializer(serializers.ModelSerializer):

    enseignants = serializers.ReadOnlyField()
    eleves = serializers.ReadOnlyField()

    class Meta:
        model = Classe
        fields = '__all__'
        depth = 4

    def create(self, validated_data):
        classe = Classe.objects.create(**validated_data)
        classe.save()
        return classe

class ClasseListSerializerFilteredEnseignant(serializers.ModelSerializer):
    enseignants = serializers.ReadOnlyField(source='classe.enseignants')
    class Meta:
        model = EnseigneAClasse
        fields = ('classe', 'enseignants')
        depth = 4

    def create(self, validated_data):
        classe = Classe.objects.create(**validated_data)
        classe.save()
        return classe

