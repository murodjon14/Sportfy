from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *


class QoshiqchiSerializer(ModelSerializer):
    class Meta:
        model = Qoshiqchi
        fields = '__all__'

class AlbomSerializer(ModelSerializer):
    class Meta():
        model = Albom
        fields = '__all__'

class QoshiqSerializer(ModelSerializer):
    class Meta:
        model = Qoshiq
        fields = '__all__'

    def validate_fayl(self, val):
        if not str(val).endswith(".mp3"):
            raise serializers.ValidationError("Faqat .mp3 fayl bolish kerak")
        return val

    def validate_devomlik(self, val):
        davomalik = str(val).split(":")
        if int(davomalik[-2]) >= 7 or int(davomalik[-3]) > 0:
            raise serializers.ValidationError("Davoma")

class Qoshiqchi_AlbomlariSerializer(serializers.ModelSerializer):
    class Meta:
        model = QoshiqchiAlbomlari
        fields = '__all__'

class AlbomQoshiqSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbomlarniQoashiqlari
        fields = '__all__'

class QoshiqSerializer(serializers.Serializer):
    class Meta:
        model = Qoshiq
        fields = '__all__'