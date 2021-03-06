from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import time
import requests
import sys

fireFoxOptions = Options()
fireFoxOptions.set_headless()

def IC_grades(username, password):

    driver = Firefox(options=fireFoxOptions)
    driver.get("https://lgca.infinitecampus.org/campus/portal/students/beachwood.jsp")
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_class_name("info").click()
    cookies = driver.get_cookies()
    driver.quit()

    s = requests.Session()
    for c in cookies:
        s.cookies[c["name"]] = c["value"]

    r = s.get("https://lgca.infinitecampus.org/campus/resources/portal/grades")
    ic_grades = r.json()
    return ic_grades[0]["terms"]

# print(IC_grades()[1]['courses'][0]['gradingTasks'][0]['progressPointsEarned'])
