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
    def test_about_page(self):
        tester = nextbook.test_client(self)
        response = tester.get('/search?filter=&q=', content_type= 'html/text')
        self.assertEqual(response.status_code, 200)
    def test_search_page(self):
        tester = nextbook.test_client(self)
        response = tester.get('/search?filter=&q=', content_type= 'html/text')
        self.assertEqual(response.status_code, 200)

    #note this may need to be changed when the book page is updated later
    def test_book_page(self):
        tester = nextbook.test_client(self)
        response = tester.get('/book/123', content_type= 'html/text')
        self.assertEqual(response.status_code, 200)
if __name__ == '__main__':
    unittest.main()
