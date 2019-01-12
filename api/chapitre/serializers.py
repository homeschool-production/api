from rest_framework import serializers
from api.models import ChapitreClasse


class ChapitreClasseSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChapitreClasse
        fields = '__all__'
        depth = 4

    def create(self, validated_data):
        chapitre = ChapitreClasse.objects.create(**validated_data)
        chapitre.save()
        return chapitre