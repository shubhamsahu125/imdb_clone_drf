from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from . import models

# Create your tests here.
class StreamPlatformTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            username="example", password="Password@123")    # Normal User
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + self.token.key)
        # creating data using model
        self.stream = models.StreamPlatform.objects.create(
            name="Netflix", about="#1 Streaming Platform", 
            website="https://www.netflix.com"
        )
    
    def test_streamplatform_create(self):
        """To verify for normal user"""
        data = {
            "name": "Netflix",
            "about": "#1 Streaming Platform",
            "website": "https://www.netflix.com"
        }
        response = self.client.post(reverse('streamplatform-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_steamplatform_list(self):
        response = self.client.get(reverse("streamplatform-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_steamplatform_ind(self):
        response = self.client.get(
            reverse("streamplatform-detail", args=(self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

class WatchListTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            username="example", password="Password@123")    # Normal User
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + self.token.key)
        # creating data using model to feed with dummy data of WatchList
        self.stream = models.StreamPlatform.objects.create(
            name="Netflix", about="#1 Streaming Platform", 
            website="https://www.netflix.com"
        )
        # creating this data to access data for testing individual or 
        # all elements of WatchList
        self.watchlist = models.WatchList.objects.create(
            platform=self.stream, title="Example Movie", 
            storyline="Example Movie", active=True) 
    
    def test_watchlist_create(self):
        """Verify that normal user's POST request is FORBIDDEN"""
        data = {
            "platform": self.stream,
            "title": "Example Movie",
            "storyline": "Example Story",
            "active": True
        }
        response = self.client.post(reverse('movie-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_watchlist_list(self):
        response = self.client.get(reverse("movie-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_watchlist_ind(self):
        response = self.client.get(
            reverse("movie-detail", args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.WatchList.objects.count(), 1)
        self.assertEqual(models.WatchList.objects.get().title, "Example Movie")


class ReviewTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            username="example", password="Password@123")    # Normal User
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.stream = models.StreamPlatform.objects.create(
            name="Netflix", about="#1 Streaming Platform", 
            website="https://www.netflix.com"
        )
        self.watchlist = models.WatchList.objects.create(
            platform=self.stream, title="Example Movie", 
            storyline="Example Movie", active=True)
        self.watchlist2 = models.WatchList.objects.create(
            platform=self.stream, title="Example Movie", 
            storyline="Example Movie", active=True) 
        self.review = models.Review.objects.create(
            review_user=self.user, rating=5, description="Great Movie!",
            watchlist=self.watchlist2, active=True
        )
    
    def test_review_create(self):
        data = {
            "review_user": self.user,
            "rating": 5,
            "description": "Great Movie!",
            "watchlist": self.watchlist,
            "active": True
        }
        response = self.client.post(
            reverse('review-create', args=(self.watchlist.id,),), data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Review.objects.count(), 2)
        # Sending POST request again to test that review can be 
        # created only once and expecting for HTTP_429_TOO_MANY_REQUESTS
        response = self.client.post(
            reverse('review-create', args=(self.watchlist.id,),), data
        )
        self.assertEqual(
            response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)
    
    def test_review_create_unauth(self):
        data = {
            "review_user": self.user,
            "rating": 5,
            "description": "Great Movie!",
            "watchlist": self.watchlist,
            "active": True
        }
        # Login as unauthenticated user because user=None
        self.client.force_authenticate(user=None)
        response = self.client.post(
            reverse('review-create', args=(self.watchlist.id,)), data
        )
        self.assertEqual(
            response.status_code, status.HTTP_401_UNAUTHORIZED
        )
    
    def test_review_update(self):
        data = {
            "review_user": self.user,
            "rating": 4,
            "description": "Great Movie! - Updated",
            "watchlist": self.watchlist,
            "active": False
        }
        response = self.client.put(
            reverse('review-detail', args=(self.review.id,)), data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_review_list(self):
        response = self.client.get(reverse('review-list', args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_ind(self):
        response = self.client.get(reverse('review-detail', args=(self.review.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_review_user(self):
        response = self.client.get(
            '/api/watch/user-reviews/?username' + self.user.username)
        self.assertEqual(response.status_code, status.HTTP_200_OK)