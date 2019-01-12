from rest_framework import serializers
from api.models import Eleve
from django.contrib.auth.models import User


class EleveSerializer(serializers.ModelSerializer):
    classes = serializers.ReadOnlyField()
    class Meta:
        model = Eleve
        fields = '__all__'
        depth = 4

    def create(self, validated_data):
        eleve = Eleve.objects.create(**validated_data)
        username = self.context["request"].data.get("username")
        password = self.context["request"].data.get("password")
        email = self.context["request"].data.get("email")
        if username and password and email:
            user = User.objects.create_user(username=username,
                                        email=email,
                                        password=password)
            eleve.user = user
            eleve.save()
        else:
            print(username, email, password)
        return eleve

