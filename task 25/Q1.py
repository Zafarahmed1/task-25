from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome WebDriver
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the IMDb search page
driver.get("https://www.imdb.com/search/name/")

# Function to wait for an element to be present and clickable
def wait_for_element(by, value):
    return WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((by, value))
    )
# Close the browser
driver.quit()