from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_homepage_and_add_question(self):
        self.browser.get('http://127.0.0.1:8000/polls/')

        # self.assertIn('Question', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('Create Question', header_text)
        #test add question
        inputbox = self.browser.find_element_by_name('addq')
        inputbox.send_keys('How do you feel?')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(4)
    def test_can_vote(self):
        pass
        # self.browser.get('http://127.0.0.1:8000/remove/')
        # q_select =self.assertIn('Who is Simon?', [row.text for row in rows])
        # q_select.delete()
        # time.sleep(10)
        # inputsubmit = self.browser.find_element_by_tag_name('input')
        # inputsubmit.send_keys('submit')
        # inputsubmit.send_keys(Keys.ENTER)
        # time.sleep(4)
        # The page updates again, and now shows both items on her list

        # table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name('tr')
        # self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        # self.assertIn(
        #     '2: Use peacock feathers to make a fly',
        #     [row.text for row in rows]
        # )
        # self.fail('Finish the test!')

if __name__ == '__main__':  
    unittest.main(warnings='ignore')