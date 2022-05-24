from rest_framework import serializers

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

        extra_kwargs = {"id": {"read_only": True}}

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)