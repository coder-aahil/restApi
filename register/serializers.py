from rest_framework import serializers
from register.models import Client,Project

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Client
        fields=['id','client_name','created_at','created_by']
    

class ProjectSerializer(serializers.ModelSerializer):
    users=ClientSerializer(many=True, read_only=True)
    class Meta:
        model=Project
        fields=['id','project_name','client','users']
        depth=1
        
