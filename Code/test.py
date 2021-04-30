from main import nextbook
import unittest

class FlaskTestCase(unittest.TestCase):

    def test_homepage(self):
        tester = nextbook.test_client(self)
        response = tester.get('/', content_type= 'html/text')
        self.assertEqual(response.status_code, 200)
    def test_classlist_page(self):
        tester = nextbook.test_client(self)
        response = tester.get('/class-list', content_type= 'html/text')
        self.assertEqual(response.status_code, 200)
    def test_add_book_page(self):
        tester = nextbook.test_client(self)
        response = tester.get('/add-book', content_type= 'html/text')
        self.assertEqual(response.status_code, 200)
    def test_about_page(self):
        tester = nextbook.test_client(self)
        response = tester.get('/about', content_type= 'html/text')
        self.assertEqual(response.status_code, 200)
    
if __name__ == '__main__':
    unittest.main()
