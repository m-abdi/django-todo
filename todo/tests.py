from http import client
from django.test import TestCase
from rest_framework.test import RequestsClient, APITestCase
from rest_framework import status
import requests

# test case with requests library client instead of apiclient
class TodoTests(APITestCase):
    def __init__(self, methodName: str = ..., *args, **kwargs) -> None:
        super().__init__(methodName)
        self.rclient = requests.Session()
        self.rrclient = RequestsClient()

    def test_login(self):
        get_resp = self.rclient.get("http://127.0.0.1:8000/users/signIn/")
        csrftoken = self.rclient.cookies["csrftoken"]
        post_resp = self.rclient.post(
            "http://127.0.0.1:8000/users/signIn/",
            data={"username": "mehdi", "pass": "1"},
            headers={"X-CSRFToken": csrftoken},
        )

        self.assertEqual(get_resp.status_code, status.HTTP_200_OK)
        self.assertEqual(post_resp.status_code, status.HTTP_200_OK)

    def test_new_todo(self):
        get_resp = self.rclient.get("http://127.0.0.1:8000/")
        csrftoken = self.rclient.cookies["csrftoken"]
        resp = self.rclient.post(
            "http://127.0.0.1:8000/",
            json={
                "taskAdd": "1",
                "title": "new todo",
                "content": "some text",
                "due_data": "2022-03-30",
                "category": "Work",
                "user": "mehdi",
            },
            headers={"X-CSRFToken": csrftoken},
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_get_todos(self):
        get_resp = self.rclient.get("http://127.0.0.1:8000/users/signIn/")
        csrftoken = self.rclient.cookies["csrftoken"]
        post_resp = self.rclient.post(
            "http://127.0.0.1:8000/users/signIn/",
            data={"username": "mehdi", "pass": "1"},
            headers={"X-CSRFToken": csrftoken},
        )
        resp = self.rclient.get(
            "http://127.0.0.1:8000/", headers={"Content-type": "application/json"}
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertGreater(len(resp.json()), 0)

    def test_edit_todo(self):
        get_resp = self.rclient.get("http://127.0.0.1:8000/users/signIn/")
        csrftoken = self.rclient.cookies["csrftoken"]
        post_resp = self.rclient.post(
            "http://127.0.0.1:8000/users/signIn/",
            data={"username": "mehdi", "pass": "1"},
            headers={"X-CSRFToken": csrftoken},
        )
        resp = self.rclient.post(
            "http://127.0.0.1:8000/todos/",
            json={
                "title": "new edited todo",
                "content": "some text",
                "due_data": "2022-03-20",
                "category": "Personal",
                "user": "mehdi",
            },
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
