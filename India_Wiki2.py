from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup ChromeDriver
print("Initializing WebDriver...")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open Wikipedia
print("Opening Wikipedia...")
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Wait to ensure page loads
time.sleep(3)

try:
    # Find the search box using XPATH (more reliable)
    print("Finding the search box...")
    search_box = driver.find_element(By.XPATH, "//input[@name='search']")

    # Ensure it's visible and ready for input
    time.sleep(2)

    # Click on the search box to make sure it's active
    search_box.click()

    # Type 'India' into the search box
    print("Typing 'India' into the search box...")
    search_box.send_keys("India")

    print("Pressing ENTER...")
    search_box.send_keys(Keys.RETURN)

    time.sleep(5)
    print("Search successful!")

except Exception as e:
    print("Error occurred:", e)

finally:
    # Close the browser after a short delay
    time.sleep(5)
    print("Closing the browser...")
    driver.quit()
