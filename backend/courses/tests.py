from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Course
class CoursesTest(TestCase):
    #automatic run
    def setUP(self):
        self.client = APIClient()
        self.course_data = {
            'name':'Python basics Course',
            'subtitle':'Python Course',
            'description':'Learn Python Basics',
            'price':30
        }
        #create course
        self.course = Course.objects.create(**self.course_data)#this do unpacking what means that this break down the informations in dictionnary
        
        #any function should start with word test so it could be excuted 
    def test_course_list(self):
        response = self.client.get('/courses/api/')
        #next line means that ther should be certain data in the page that means that the code is right and the test is succeful
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    def test_course_detail(self):
        response = self.client.get('/courses/api/1/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)