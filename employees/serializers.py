from rest_framework import serializers

from addresses.serializers import AddressSerializer
from contracts.serializers import ContractSerializer
from personal_documents.serializers import PersonalDocumentSerializer

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

        extra_kwargs = {
            "id": {"read_only": True},
            "contract": {"required": False},
            "personal_documents": {"required": False},
            "address": {"required": False},
        }

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

class EmployeeDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
    
    contract = ContractSerializer()
    personal_documents = PersonalDocumentSerializer()
    address = AddressSerializer()
