# -*- coding: utf-8 -*-
from django.test import TestCase

from courses.models import Course, Lesson


class CoursesTests(TestCase):

	def test_course_list(self):
		from django.test import Client

		client = Client()
		response = client.get('/')		
		self.assertEqual(response.status_code, 200)
		self.assertEqual(Course.objects.all().count(), 0)


		course1 = Course.objects.create(
			title = 'Testing title', 
			short_description = 'Testing short description',
			description = 'Testing description'
			)

		self.assertEqual(Course.objects.all().count(), 1)
		response = client.get('/')
		self.assertContains(response, 'Testing title')
		

	def test_course_page(self):
		from django.test import Client

		client = Client()
		response = client.get('/courses/1/')
		self.assertEqual(response.status_code, 404)

		course1 = Course.objects.create(
			title = 'Testing title', 
			short_description = 'Testing short description',
			description = 'Testing description'
			)

		response = client.get('/courses/1/')		
		self.assertEqual(response.status_code, 200)
		self.assertEqual(Course.objects.all().count(), 1)
