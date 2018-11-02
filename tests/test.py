from src.app import create_app
import os
import unittest
from base64 import b64encode


class TestCase(unittest.TestCase):
	def test_index(self):
		env_name = os.getenv('FLASK_ENV')
		print(env_name)
		app = create_app(env_name)
		tester = app.test_client(self)
		tester.testing = True
		headers = {
			'Authorization': 'Basic %s' % b64encode("{0}:{1}".format('admin', 'admin').encode('utf-8'))
		}
		response = tester.get('/login', headers=headers)
		print(response)
		self.assertEqual(200, response.status_code)
