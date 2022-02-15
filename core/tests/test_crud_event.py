from core.models import User
from django.test.client import Client
from django.test.testcases import TestCase
from core.tests import fixtures
import json


class TestCrudEvent(TestCase):
    @classmethod
    def setUpTestData(cls):
        fixtures.user_jon()

    def test_auth_api(self):
        client = Client()
        client.force_login(User.objects.get(username='jon'))
        self._addevent(client, 'Joseph is born')
        self._addevent(client, 'Rachel dies')
        self._addevent(client, 'Joseph is sold into slavery')
        self._list_events_assert_count(3, ['Joseph is born'], ['Rachel dies'], ['Joseph is sold into slavery'])
        self._list_events_update_event(1, 'Rachel dies in labor')
        self._list_events_assert_count(3, ['Joseph is born'], ['Rachel dies in labor'], ['Joseph is sold into slavery'])
        self._list_events_remove(1)
        self._list_events_assert_count(2, ['Joseph is born'], ['Rachel dies'], ['Joseph is sold into slavery'])

    def _addevent(self, client, description):
        event = {
            'description': description,
            'source': 'Torah',
            'age': 13,
            'sourceAge': 'Rashi'
        }
        r = client.post('/api/events/save', {'event': json.dumps(event)})
        self.assertEqual(200, r.status_code)
        # r1 = client.post('/api/add_todo', {'new_task': 'walk the dog'})
        # r2 = client.post('/api/add_todo', {'new_task': 'do the laundry'})
        # r3 = client.get('/api/list_todos')
        # self.assertEqual({200}, {r.status_code for r in [r1, r2, r3]})
        # todos = json.loads(r3.content.decode('utf-8'))
        # self.assertEqual(2, len(todos['todos']))

