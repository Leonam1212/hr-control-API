from rest_framework.exceptions import ValidationError, AuthenticationFailed
from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from .permissions import IsRH
from .models import Account
from .serializers import LoginSerializer,AccountSerializer

    
class AccountView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsRH]

    queryset = Account.objects
    serializer_class = AccountSerializer

class AccountUpdateAndDeleteView(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsRH]

    queryset = Account.objects
    serializer_class = AccountSerializer
    lookup_field = 'id'

class LoginView(APIView):
    serializer_class = LoginSerializer
    def post(self, request: Request):
        try:
            token = LoginSerializer(data=request.data).authenticate()
            return Response({"token": token})
        except (ValidationError, AuthenticationFailed) as err:
            return Response(err.detail, err.status_code)
