from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        # She is invited to enter a to-do item straight away.
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-do item.'
        )

        # She types "Buy Peacock feathers" (her hobby is tying fly-fishing lures).
        input_box.send_keys('Buy peacock feathers.')

        # When she hits enter, the page updates and now the page lists
        # "1: Buy Peacock feathers" as an item on her to-do list.
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers.' for row in rows)
        )

        # There is still a text box inviting her to enter another item.
        # She enters "Use Peacock feathers to make a fly".
        self.fail('Finish this test.')

        # The page updates, and now shows both items on her to-do list.

        # Edith wonders if the site will remember her list. Then she sees that
        # the site has generated a random URL for her -- there is some explanatory
        # text to that effect.

        # She visits that URL and her to-do list is still there.

if __name__ == '__main__':
    unittest.main()