from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# ensures the correct ChromeDriver is downloaded & used automatically
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# open Google
driver.get("https://www.google.com")

# print the page title in the console
print("Page title is:", driver.title)

# close Chrome
driver.quit()
