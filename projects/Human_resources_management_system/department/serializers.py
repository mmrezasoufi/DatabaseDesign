from rest_framework import serializers
from .models import Department, Building


class DepartmentSerializer(serializers.ModelSerializer):

    director = serializers.CharField(source="director.user.username")
    created = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ("director", "name", "created")

    def get_created(self, obj):
        return obj.created.date()    
    

class BuildingSerializer(serializers.ModelSerializer):

    created = serializers.SerializerMethodField()

    class Meta:
        model = Building
        fields = ("city", "zone", "address", "created")

    def get_created(self, obj):
        return obj.created.date()
    