import unittest

from app import app

class AppTest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

        self.assertEqual(app.debug, False)

    def tearDown(self):
        pass
    
    def test_root(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_yearly_data_list(self):
        response = self.app.get('/yearly',  follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'2020', response.data)
        self.assertIn(b'2021', response.data)

    def test_specific_year_data(self):
        response = self.app.get('/yearly/2020',  follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'2020', response.data)
        self.assertNotIn(b'2021', response.data)

    def test_monthly_data_list(self):
        response = self.app.get('/monthly',  follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'2021-05', response.data)
        self.assertIn(b'2020-12', response.data)

    def test_monthly_data_by_year(self):
        response = self.app.get('/monthly/2021',  follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'2021-05', response.data)
        self.assertNotIn(b'2020-12', response.data)
    
    def test_specific_monthly_data(self):
        response = self.app.get('/monthly/2020/05',  follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'2020-05', response.data)
        self.assertNotIn(b'2020-12', response.data)

    def test_daily_data_list(self):
        response = self.app.get('/daily',  follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'2020-12-12', response.data)
        self.assertIn(b'2020-07-12', response.data)
        self.assertIn(b'2021-12-12', response.data)

    def test_daily_data_by_year(self):
        response = self.app.get('/daily/2020',  follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'2020-12-12', response.data)
        self.assertIn(b'2020-07-12', response.data)
        self.assertNotIn(b'2021-12-12', response.data)


    def test_daily_data_by_month(self):
        response = self.app.get('/daily/2020/04',  follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'2020-04-13', response.data)
    
    def test_specific_daily_data(self):
        response = self.app.get('/daily/2020/04/13',  follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'2020-04-13', response.data)

if __name__ == "__main__":
    unittest.main()
