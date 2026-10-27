from django.test import TestCase
from django.urls import reverse
from stories.models import Topic, Story


class StoryPageTests(TestCase):
    def setUp(self):
        self.topic = Topic.objects.create(
            name='Общество',
            description='Обществени теми',
        )
        self.story = Story.objects.create(
            topic=self.topic,
            title='Тестов материал',
            summary='Кратко резюме',
            status='draft',
        )

    def test_story_list_loads(self):
        response = self.client.get(reverse('story_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Тестов материал')

    def test_story_detail_loads(self):
        response = self.client.get(
            reverse('story_detail', args=[self.story.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Тестов материал')

    def test_topic_list_loads(self):
        response = self.client.get(reverse('topic_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Общество')

    def test_story_create_page_loads(self):
        response = self.client.get(reverse('story_create'))
        self.assertEqual(response.status_code, 200)

    def test_topic_create_page_loads(self):
        response = self.client.get(reverse('topic_create'))
        self.assertEqual(response.status_code, 200)
