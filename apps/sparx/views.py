from rest_framerwork import viwesets
from .models import Student
from .serializers import StudentSerializer
from django.shortcuts import render

class StudentViewSet(viwesets.ModelViewSet):
    queryset = Student.objects.all
    serializer = StudentSerializer

