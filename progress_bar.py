import unittest
from selenium import webdriver

class TestProgressBarOnApprovedBrowsers (unittest.TestCase):
    driver = webdriver.browser('browser path')
    driver.get("https://myurl.com")
    progress_bar = driver.find_element_by_xpath("xpath string here")
    assert "progress bar jpg"