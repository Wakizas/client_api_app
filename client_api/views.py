from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import DestroyAPIView
from .models import Client
from .serializers import ClientSerializer

#Endpoint for (R)ead Client
class ClientListViews(ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

#Endpoint for (C)reate Client
class ClientAddViews(CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

#Endpoint for (U)pdate Client
class ClientUpdateViews(UpdateAPIView):
    lookup_field = "matricule"
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

#Endpoint for (C)reate Client
class ClientDeleteViews(DestroyAPIView):
    lookup_field = "matricule"
    queryset = Client.objects.all()
    serializer_class = ClientSerializer