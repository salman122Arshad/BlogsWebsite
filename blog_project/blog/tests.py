from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post

class PostModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post.',
            author=self.user
        )

    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)

    def test_post_create_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('post_new'), {
            'title': 'New Post',
            'content': 'Content for the new post.',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success

    def test_post_edit_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('post_edit', kwargs={'pk': self.post.pk}), {
            'title': 'Updated Post',
            'content': 'Updated content for the post.',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success

    def test_post_delete_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('post_delete', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 302)  # Redirect after success
