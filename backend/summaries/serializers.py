from .models import DailySummary, ExcitedAbout
from rest_framework import serializers
from project.serializers import UserSerializer

class StringListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExcitedAbout
        fields =('value', 'id')

class DailySummarySerializer(serializers.HyperlinkedModelSerializer):
    excited_about = StringListSerializer(many=True)
    user = UserSerializer()

    class Meta:
        model = DailySummary
        fields = (
            'affirmation',
            'id',
            'excited_about',
            'user',
            'created',
            'date' )