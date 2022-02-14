# https://faun.pub/how-to-install-selenium-in-linux-e8928b2b709
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import datetime
import time

# Set path Selenium
CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
s = Service(CHROMEDRIVER_PATH)
WINDOW_SIZE = "1920,1080"

# Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(service=s, options=chrome_options)

dt = datetime.datetime.now()

driver.get("https://google.com")
time.sleep(3)
driver.save_screenshot("screenshots/google.com/{}_google.png".format(dt.strftime("%d_%m_%Y")))
driver.get("https://duckduckgo.com")
time.sleep(3)
driver.save_screenshot("screenshots/duckduckgo.com/{}_duckduckgo.png".format(dt.strftime("%d_%m_%Y")))
driver.get("https://twitter.com")
time.sleep(3)
driver.save_screenshot("screenshots/twitter.com/{}_twitter.png".format(dt.strftime("%d_%m_%Y")))
driver.get("https://en.wikipedia.org")
time.sleep(3)
driver.save_screenshot("screenshots/en.wikipedia.org/{}_wikipedia.png".format(dt.strftime("%d_%m_%Y")))
driver.get("https://github.com")
time.sleep(3)
driver.save_screenshot("screenshots/github.com/{}_github.png".format(dt.strftime("%d_%m_%Y")))
driver.get("https://xkcd.com")
time.sleep(3)
driver.save_screenshot("screenshots/xkcd.com/{}_xkcd.png".format(dt.strftime("%d_%m_%Y")))
driver.get("https://nasa.gov")
time.sleep(3)
driver.save_screenshot("screenshots/nasa.gov/{}_nasa.png".format(dt.strftime("%d_%m_%Y")))
driver.get("https://eff.org")
time.sleep(3)
driver.save_screenshot("screenshots/eff.org/{}_eff.png".format(dt.strftime("%d_%m_%Y")))
driver.get("https://yahoo.com")
time.sleep(3)
driver.save_screenshot("screenshots/yahoo.com/{}_yahoo.png".format(dt.strftime("%d_%m_%Y")))
time.sleep(2)
driver.close()
