import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from seletools.actions import drag_and_drop

@pytest.fixture
def driver():
    # Set up the WebDriver instance
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    # Teardown - close the WebDriver instance
    driver.quit()

def test_drag_and_drop(driver):
    # Navigate to the HTML file
    driver.get("http://the-internet.herokuapp.com/drag_and_drop")
    #driver.find_element(By.LINK_TEXT, 'Drag and Drop').click()

    # Find the draggable and droppable elements
    src_element = driver.find_element(By.ID,'column-a')
    target_element = driver.find_element(By.ID, 'column-b')
    time.sleep(2)
    drag_and_drop(driver,src_element,target_element)
    time.sleep(2)
    # Perform the drag and drop operation
    #action_chains = ActionChains(driver)
    #action_chains.drag_and_drop(src_element, target_element).perform()
    #time.sleep(3)
   # action_chains.drag_and_drop(target_element,src_element)
    #action_chains.perform()
    #action_chains.click_and_hold(src_element).pause(3).move_to_element(target_element).perform() # another way to perform drag and drop

    # Verify that Tile A is listed to the right of Tile B by getting the headers of tile-A and tile-B
    tile_a = driver.find_element(By.CSS_SELECTOR,'#column-a header').text
    tile_b = driver.find_element(By.CSS_SELECTOR,'#column-b header').text
    assert tile_a == 'B',f"Expected : B. but found:A"
    assert tile_b == 'A',f"Expected : A. but found:B"



