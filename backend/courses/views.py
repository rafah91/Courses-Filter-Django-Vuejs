from rest_framework import generics
from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import CourseSerializer , CategorySerializer
from .models import Course , Category
from .filters import CourseFilter



class CourseListAPI(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']
    filterset_class = CourseFilter
    

    
    
class CourseDetailAPI(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    
    
class CategoryListAPI(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
