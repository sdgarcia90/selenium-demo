from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# jump straight to results page for "Selenium Python"
driver.get("https://www.google.com/search?q=Selenium+Python")

print("Results page title is:", driver.title)

driver.quit()
