from rest_framework import serializers
from api.models import Question


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'
        depth = 4

    def create(self, validated_data):
        question = Question.objects.create(**validated_data)
        question.save()
        return question