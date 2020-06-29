from rest_framework import viewsets

from .serializers import MyanUserSerializer
from .models import MyanUser


class MyanUserViewSet(viewsets.ModelViewSet):
    queryset = MyanUser.objects.all()
    serializer_class = MyanUserSerializer