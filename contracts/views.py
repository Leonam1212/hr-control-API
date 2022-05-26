from django.core.exceptions import ObjectDoesNotExist
from django.forms import ValidationError
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

from employees.models import Employee
from .models import Contract
from .serializers import ContractSerializer
from accounts.permissions import IsRH


class CreateContractView(generics.GenericAPIView):
    # permission_classes = [IsRH]

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

    def post(self, request: Request, employee_id=""):
        try:
            serialized: ModelSerializer = self.get_serializer(data=request.data)
            serialized.is_valid(True)

            employee = Employee.objects.filter(pk=employee_id)

            if not employee:
                raise ObjectDoesNotExist

            if employee.first().contract:
                return Response(
                    {"detail": "Employee already has a contract"},
                    status.HTTP_422_UNPROCESSABLE_ENTITY,
                )

            new_contract = serialized.save()

            employee.update(contract=new_contract)
            employee.first().save()

            return Response(serialized.data, status.HTTP_201_CREATED)

        except (ValidationError, ObjectDoesNotExist):
            return Response({"detail": "Not found"}, status.HTTP_404_NOT_FOUND)


class ListContractView(generics.ListAPIView):
    # permission_classes = [IsRH]

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    lookup_field = "id"


class UpdateAndDeleteContractView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsRH]

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    lookup_field = "id"