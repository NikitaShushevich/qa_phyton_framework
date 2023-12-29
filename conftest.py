import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(ChromeDriverManager(version="120.0.6099").install())
    driver.get("http://www.python.org")
    driver.maximize_window()
    yield driver
    driver.quit()
