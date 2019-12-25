from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith goes to the homepage of a new to-do app.
        self.browser.get('http://localhost:8000')
        # She notices the page title and the header mention to-do lists.
        assert 'To-Do' in self.browser.title
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish this test.')
        # She is invited to enter a to-do item straight away.

        # She types "Buy Peacock feathers" (her hobby is tying fly-fishing lures).

        # When she hits enter, the page updates and now the page lists
        # "1: Buy Peacock feathers" as an item on her to-do list.

        # There is still a text box inviting her to enter another item.
        # She enters "Use Peacock feathers to make a fly".

        # The page updates, and now shows both items on her to-do list.

        # Edith wonders if the site will remember her list. Then she sees that
        # the site has generated a random URL for her -- there is some explanatory
        # text to that effect.

        # She visits that URL and her to-do list is still there.

if __name__ == '__main__':
    unittest.main()