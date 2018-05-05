from django.test import TestCase
#from api.models import Song
#from rest_framework.test import APIClient, RequestsClient

# Create your tests here.
# class SongTest(TestCase):
#     """ Test for Crash model """

#     fixtures = ['songs']

#     def test_song_returns_title(self):
#         song = Song.objects.get(pk=1)
#         self.assertEqual(song.title, "Ripple")
#     def test_song_returns_albumn(self):
#         song = Song.objects.get(pk=1)
#         self.assertEqual(song.album, "American Beauty")
#     def test_song_returns_release_date(self):
#         song = Song.objects.get(pk=2)
#         self.assertEqual(str(song.release_date), "1978-11-15 07:00:00+00:00")
#     def test_song_returns_writer(self):
#         song = Song.objects.get(pk=3)
#         self.assertEqual(song.writer, "Weir, Barlow")

# class SongEndpointsTestCase(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#     def test_list_200_response(self):
#         response = self.client.get('/api/songs/')
#         self.assertEqual(response.status_code, 200)
#     def test_list_404_response(self):
#         response = self.client.get('/api/songz/')
#         self.assertEqual(response.status_code, 404)
