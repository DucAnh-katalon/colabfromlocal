
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common import by

service = ChromeService()  # type: ignore
chrome_options = ChromeOptions()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("profile.cookie_controls_mode 0")
chrome_options.add_argument("--allow-third-party-cookies")
chrome_options.add_experimental_option("profile.cookie_controls_mode", 0);
driver = Chrome(service = service)
driver.get("https://www.golem.de/news/1-mai-ist-streiken-noch-zeitgemaess-in-der-agilen-it-branche-2405-184679.html")
