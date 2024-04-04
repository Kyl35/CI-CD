import unittest
from app import app

class FlaskTestCase(unittest.TestCase):

  def setUp(self):
    self.app = app.test_client()
    self.app.testing = True
    
  def test_home_status_code(self):
    response = self.app.get('/')
    self.assertEqual(response.status_code, 200)

  def test_info_status_code(self):
    response = self.app.get('/info')
    self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
  unittest.main()
