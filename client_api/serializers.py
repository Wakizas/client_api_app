from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    matricule = serializers.CharField()
    nom = serializers.CharField()
    prenoms = serializers.CharField()
    tel = serializers.CharField()

    class Meta:
        model = Client
        fields = ['matricule', 'nom', 'prenoms', 'tel']