# tests/test_app.py
import sys
import os
import json
import unittest

# Add the parent directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

class TestMLApp(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_health_endpoint(self):
        response = self.app.get('/health')
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'healthy')
    
    def test_predict_endpoint(self):
        # Test with a sample feature vector
        test_data = {
            'features': [0, 1]
        }
        response = self.app.post('/predict', 
                                 data=json.dumps(test_data),
                                 content_type='application/json')
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('prediction', data)
        self.assertIsInstance(data['prediction'], list)


if __name__ == '__main__':
    unittest.main()