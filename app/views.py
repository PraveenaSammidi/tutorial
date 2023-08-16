from django.shortcuts import render
from rest_framework import viewsets
from .models import Members
from .serializers import MemberSerializer




class MemberViewSet(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer
