import os
import requests
import unittest

from coverage import coverage

cov = coverage(branch=True, omit=['flask/*', 'tests.py'])
cov.start()


class TestApi(unittest.TestCase):
    def setUp(self):
        self.api_url = 'http://localhost:5000/api/v1.0'

    def test_favorites_get(self):
        r = requests.get(self.api_url + '/favorites')
        return self.assertEqual(r.status_code, 200)

    def test_favorites_post(self):
        r = requests.get(self.api_url + '/favorites')
        return self.assertEqual(r.status_code, 201)

    def test_latest_get(self):
        r = requests.get(self.api_url + '/latest')
        return self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()

    cov.stop()
    cov.save()
    print("\n\nCoverage Report:\n")
    cov.report()
    print("HTML version: " + os.path.join(os.path.basedir, "tmp/coverage/index.html"))
    cov.html_report(directory='tmp/coverage')
    cov.erase()