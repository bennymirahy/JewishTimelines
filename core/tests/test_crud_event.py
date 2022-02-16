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
        self._list_events_assert_count(client, 3, ['Joseph is born', 'Rachel dies', 'Joseph is sold into slavery'])
        self._list_events_update_event(client, 1, 'Rachel dies in labor')
        self._list_events_assert_count(client, 3, ['Joseph is born', 'Rachel dies in labor', 'Joseph is sold into slavery'])
        self._list_events_remove(client, 1)
        self._list_events_assert_count(client, 2, ['Joseph is born', 'Joseph is sold into slavery'])
        self._list_pais_and_get(client, 1, 'Joseph is sold into slavery')

    def _addevent(self, client, description):
        event = {
            'description': description,
            'source': 'Torah',
            'age': 13,
            'sourceAge': 'Rashi'
        }
        r = client.post('/api/events/save', {'event': json.dumps(event)})
        self.assertEqual(200, r.status_code)

    def _list_events_assert_count(self, client, count, expectedDescriptions):
        r = client.get('/api/events')
        self.assertEqual(200, r.status_code)
        events = json.loads(r.content.decode('utf-8'))
        self.assertEqual(count, len(events))
        self.assertEqual(expectedDescriptions, [e['description'] for e in events])

    def _list_events_update_event(self, client, idx, newDescription):
        r = client.get('/api/events')
        self.assertEqual(200, r.status_code)
        events = json.loads(r.content.decode('utf-8'))
        event = events[idx]
        event['description'] = newDescription
        self.assertTrue('id' in event)
        r = client.post('/api/events/save', {'event': json.dumps(event)})
        self.assertEqual(200, r.status_code)

    def _list_events_remove(self, client, idx):
        r = client.get('/api/events')
        self.assertEqual(200, r.status_code)
        events = json.loads(r.content.decode('utf-8'))
        event = events[idx]
        r = client.post('/api/events/%s/remove' % event['id'])
        self.assertEqual(200, r.status_code)

    def _list_pais_and_get(self, client, idx, expectedDescription):
        r = client.get('/api/events')
        self.assertEqual(200, r.status_code)
        events = json.loads(r.content.decode('utf-8'))
        event = events[idx]
        r = client.get('/api/events/%s' % event['id'])
        self.assertEqual(200, r.status_code)
        event = json.loads(r.content.decode('UTF-8'))
        self.assertEqual(expectedDescription, event['description'])


        # r1 = client.post('/api/add_todo', {'new_task': 'walk the dog'})
        # r2 = client.post('/api/add_todo', {'new_task': 'do the laundry'})
        # r3 = client.get('/api/list_todos')
        # self.assertEqual({200}, {r.status_code for r in [r1, r2, r3]})
        # todos = json.loads(r3.content.decode('utf-8'))
        # self.assertEqual(2, len(todos['todos']))

