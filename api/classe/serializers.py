from rest_framework import serializers
from api.models import Classe


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

