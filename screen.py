from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://google.com")
driver.save_screenshot("google.png")
driver.close()
