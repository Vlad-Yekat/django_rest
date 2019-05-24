from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from insidepages.models import MixPost
from rest_framework.reverse import reverse as api_reverse


class MixPostAPITestCase(APITestCase):
    def set_up(self):
        pass

    def test_count(self):
        post_all = MixPost.objects.count()
        self.assertGreater(post_all, 1)

    def test_1_MixPost_ListAll_Return_0(self):
        url = reverse('mixpost-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(MixPost.objects.all().count(), 0)

    def test_2_MixPost_ListSingle_Return_0(self):
        url = reverse('mixpost-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(MixPost.objects.filter(Name__contains=self._value).count(), 0)

    def test_3_MixPost_Post_ReturnNothing(self):
        url = reverse('mixpost-list')
        data = {'Name': self._value}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MixPost.objects.filter(Name__contains=self._value).count(), 1)

    def test_4_MixPost_Update_ReturnRecordUpdated(self):
        url = reverse('mixpost-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, )
        result = MixPost.objects.get(Name__contains=self._value).values_list('id')
        self.assertEqual(MixPost.objects.count(), 1, )

