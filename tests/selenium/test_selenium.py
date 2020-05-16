import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup_chromedriver")
class TestSelenium:
    def test_page_title(self):
         assert "nolla.net" in self.driver.title