from django.http import HttpRequest
from rest_framework import generics
from accounts.permissions import IsRH
from .tools import getPdf, getAllPdfs
from .models import Candidate
from .serializers import CandidateSerializer


class CandidateView(generics.ListCreateAPIView):
    # permission_classes = [IsRH]
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    
    def get(self, request, *args, **kwargs):
        try:           
            return getAllPdfs()
        except FileNotFoundError:
            return self.list(request, *args, **kwargs)

class UpdateDestroyCandidateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        try:
            getPdf(self)
            return self.retrieve(request, *args, **kwargs)
        except FileNotFoundError:
            return self.retrieve(request, *args, **kwargs)