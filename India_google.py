from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
print("Initializing WebDriver...")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open Google
print("Opening Google...")
driver.get("https://www.bing.com")

try:
    # Wait for the search box to appear
    print("Waiting for search box...")
    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "q"))
    )

    # Type 'India' into the search box
    print("Typing 'India' into search box...")
    search_box.send_keys("India")

    # Wait for the Google Search button to be clickable
    print("Waiting for search button...")
    search_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.NAME, "btnK"))
    )

    # Click the search button
    print("Clicking search button...")
    search_button.click()

    # Wait for search results to load
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "search"))
    )

    print("Search completed successfully!")

except Exception as e:
    print("Error:", e)

finally:
    # Wait before closing
    WebDriverWait(driver, 5)

    # Close the browser
    print("Closing browser...")
    #driver.quit()
