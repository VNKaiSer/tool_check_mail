from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from faker import Faker
import random
import string

def create_profile_google():
    fist_name = Faker().first_name()
    last_name = Faker().last_name()
    password = Faker().password()
    add_email = str(random.randint(1000, 9999)) + ''.join(random.choices(string.ascii_lowercase, k=5))
    email = f"{fist_name}.{last_name}{add_email}@gmail.com"
    date = random.randint(1, 28)
    month = random.randint(1, 12)
    year = random.randint(1980, 2000)
    sex = Faker().random_element(["F", "M"])

    data = {
        "firstName": fist_name,
        "lastName": last_name,
        "password": password,
        "email": email,
        "date": date,
        "month": month,
        "year": year,
        "sex": sex
    }
    return data
def start_task(): 
    # Cấu hình Chrome
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--profile-directory=Default")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--disable-infobars")
    
    # Khởi chạy trình duyệt với proxy
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://accounts.google.com/signup")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'firstName')))
    

    input("Enter to close:")
    driver.quit()
# start_task()
print(create_profile_google())
